import os
import pandas as pd

from cryptofees.CryptoFees import CryptoFees
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    """
    This function pulls crypto fees from crypto fees
    """

    crypto_fees = CryptoFees()
    ids = pd.read_csv(crypto_fees.id_csvs).id.tolist()

    for id_ in ids:
        df = crypto_fees.pull_crypto_fees(id_)
        df.to_csv(os.path.join(crypto_fees.data_folder, f"{id_}.csv"), index=False)
