from cryptofees.CryptoFees import CryptoFees
from util.time_series import smoothing_rolling_window

if __name__ == "__main__":
    """
    This function plots all AAVE revenues
    """
    crypto_fees = CryptoFees()
    aave = crypto_fees.load_data("aave")
    aave = smoothing_rolling_window(aave, "fee", 30)
    crypto_fees.plot_crypto_fees(aave, "AAVE", "aave.png", ylim=[0, 10 * (10**6)])
