import pandas as pd


def smoothing_rolling_window(
    df: pd.DataFrame, column_name: str, days: int
) -> pd.DataFrame:
    """
    smooths the earnings with a rolling window of 30 days
    """
    df["rolling"] = df[column_name].rolling(days).mean()
    df = df[~df["rolling"].isna()]
    df.pop(column_name)
    df = df.rename(columns={"rolling": column_name})
    return df
