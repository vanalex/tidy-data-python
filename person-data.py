import pandas as pd

df = pd.read_csv('./data/person-score.csv')
print(df)

melted = pd.melt(df, id_vars=["weekday"], var_name="Person", value_name="Score")
print(melted.head(50))