import pandas as pd

df = pd.read_csv('./data/pew-raw.csv')
print(df)

formatted_df = pd.melt(df, ['religion'], var_name = 'income', value_name = 'freq')
formatted_df = formatted_df.sort_values(by=['religion'])
print(formatted_df.head(50))