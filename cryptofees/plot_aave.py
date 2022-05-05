from cryptofees.CryptoFees import CryptoFees
from coingecko.CoinGecko import CoinGecko
from util.time_series import smoothing_rolling_window

if __name__ == "__main__":
    """
    This function plots all AAVE revenues
    """
    crypto_fees = CryptoFees()
    coingecko = CoinGecko()
    aave = crypto_fees.load_data("aave")
    market_cap = coingecko.load_data("uniswap")
    market_cap = smoothing_rolling_window(market_cap, "market_caps", 30)
    aave = smoothing_rolling_window(aave, "fee", 30)

    corr = aave.fee.corr(market_cap.market_caps)
    print(f"Revenue Market Cap Corr: {corr}")
    crypto_fees.plot_crypto_fees_super_impose(
        aave, market_cap, "aave.png", ylim=[0, 10 * (10**6)]
    )
