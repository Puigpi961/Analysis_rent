
import pandas as pd

df = pd.read_csv(
    "data/apartments_for_rent_classified_10K.csv",
    encoding="cp1252",
    sep=";"
)

print(df.head())
print(df.shape)
print(df.columns)
print(df["state"].unique())