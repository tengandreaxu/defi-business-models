import pandas as pd

if __name__ == "__main__":
    """
    simply converts the response from get_cryptofeess_tokens.sh
    into csv
    """

    with open("data/cryptofees_tokens.json") as file_:
        raw = file_.readlines()
        raw_python = eval(raw[0].replace("true", "True").replace("null", "None"))
        df = pd.DataFrame(raw_python["protocols"])
        df.to_csv("./data/cryptofees_tokens.csv", index=False)
