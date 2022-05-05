import os
import json
import pandas as pd
from datetime import datetime
from dataclasses import dataclass
from cryptofees.CryptoFees import END_DATE


@dataclass
class CoinGecko:
    def __init__(self):
        self.data_folder = "data/coingecko"

    def load_data(self, token: str) -> pd.DataFrame:

        with open(os.path.join(self.data_folder, f"{token}.json")) as f:
            data = json.load(f)
            df = pd.DataFrame(data)

        df["timestamp"] = df.prices.apply(lambda x: x[0])
        df["prices"] = df.prices.apply(lambda x: x[1])
        df["market_caps"] = df.market_caps.apply(lambda x: x[1])
        df["total_volumes"] = df.total_volumes.apply(lambda x: x[1])
        df["date"] = df.timestamp.apply(
            lambda x: datetime.fromtimestamp(x / 1000)
        ).dt.date
        df = df[df.date <= END_DATE]

        return df
