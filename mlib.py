import os
import pandas as pd
from tabulate import tabulate


def load_df(file=os.path.join("data", "stats.csv")):
    return pd.read_csv(file, index_col=0)


def get_closest(_p, _r, _a):
    df = load_df()
    dev = (
        df["PPG"].subtract(_p).pow(2)
        + df["RPG"].subtract(_r).pow(2)
        + df["APG"].subtract(_a).pow(2)
    )
    result = df.loc[dev.sort_values().head(5).index]
    return tabulate(result[["NAME", "TEAM", "GP", "PPG", "RPG", "APG"]], headers="keys")
