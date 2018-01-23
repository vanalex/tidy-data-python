import pandas as pd
import datetime

df = pd.read_csv('./data/weather-raw.csv')
print(df)

df = pd.melt(df, id_vars=["id", "year","month","element"], var_name="day_raw")
df.head(10)

# Extracting day
df["day"] = df["day_raw"].str.extract("d(\d+)", expand=False)
df["id"] = "MX17004"

# To numeric values
df[["year","month","day"]] = df[["year","month","day"]].apply(lambda x: pd.to_numeric(x, errors='ignore'))

# Creating a date from the different columns
def create_date_from_year_month_day(row):
    return datetime.datetime(year=row["year"], month=int(row["month"]), day=row["day"])

df["date"] = df.apply(lambda row: create_date_from_year_month_day(row), axis=1)
df = df.drop(['year',"month","day", "day_raw"], axis=1)
df = df.dropna()

# Unmelting column "element"
df = df.pivot_table(index=["id","date"], columns="element", values="value")
df.reset_index(drop=False, inplace=True)
print('')
print(df)