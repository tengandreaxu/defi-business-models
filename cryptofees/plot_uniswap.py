from cryptofees.CryptoFees import CryptoFees
from coingecko.CoinGecko import CoinGecko
from util.time_series import smoothing_rolling_window

if __name__ == "__main__":
    """
    This function plots all Uniswap revenues
    """
    crypto_fees = CryptoFees()
    coingecko = CoinGecko()

    market_cap = coingecko.load_data("uniswap")
    df = crypto_fees.load_data("uniswap")
    df = smoothing_rolling_window(df, "fee", 30)
    market_cap = smoothing_rolling_window(market_cap, "market_caps", 30)
    corr = df.fee.corr(market_cap.market_caps)
    print(f"Revenue Market Cap Corr: {corr}")
    crypto_fees.plot_crypto_fees_super_impose(
        df, market_cap, "uni.pdf", titel="UNI", ylim=[0, 10 * (10**6)]
    )
