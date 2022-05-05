import pandas as pd
from datetime import datetime
from coingecko.CoinGecko import CoinGecko
from cryptofees.CryptoFees import CryptoFees
from util.time_series import smoothing_rolling_window


def get_yearn_time_series() -> pd.DataFrame:
    """
    Reads and clean YFI revenue data
    """
    file_path = "yearn_revenues/yearn_revenues_data"
    with open(file_path) as file_:
        data = file_.readlines()
        data_python = eval(data[0].replace("true", "True").replace("null", "None"))

    results = data_python["results"][0]["result"]["data"]["dsr"]["DS"][0]["PH"][0][
        "DM0"
    ]
    time_series = [x["C"] for x in results]

    # *******************
    # data is very bad structured
    # ******************
    first_element = time_series.pop(0)[4:]
    clean = [x[-2:] for x in time_series]

    final_df = [
        {
            "fee": float(first_element[0]),
            "date": datetime.fromtimestamp(first_element[1] / 1000).date(),
        }
    ]

    for x in clean:

        final_df.append(
            {
                "fee": float(x[0]),
                "date": datetime.fromtimestamp(x[1] / 1000).date(),
            }
        )
    df = pd.DataFrame(final_df)
    return df


if __name__ == "__main__":
    """
    Plots YFI revenue
    """
    yearn = get_yearn_time_series()
    coingecko = CoinGecko()
    market_cap = coingecko.load_data("yearn")
    market_cap = smoothing_rolling_window(market_cap, "market_caps", 30)
    yearn = smoothing_rolling_window(yearn, "fee", 30)
    yearn = yearn[yearn.date < datetime.fromisoformat("2021-12-02").date()]
    corr = yearn.fee.corr(market_cap.market_caps)
    print(f"Revenue Market Cap Corr: {corr}")
    crypto_fees = CryptoFees()

    crypto_fees.plot_crypto_fees_super_impose(
        yearn, market_cap, "yearn.png", use_millions_ax2=True, ylim=[0, 10 * (10**6)]
    )
