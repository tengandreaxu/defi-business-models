from cryptofees.CryptoFees import CryptoFees
from util.time_series import smoothing_rolling_window

if __name__ == "__main__":
    """
    This function plots all Uniswap revenues
    """
    crypto_fees = CryptoFees()

    df = crypto_fees.load_data("uniswap")
    df = smoothing_rolling_window(df, "fee", 30)
    crypto_fees.plot_crypto_fees(df, "UNI", "uni.png", ylim=[0, 10 * (10**6)])
