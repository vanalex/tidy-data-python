import pandas as pd

df = pd.read_csv('./data/tb-raw.csv')
print(df)

df = pd.melt(df, id_vars=["country", "year"], value_name="cases", var_name="sex_and_age")


