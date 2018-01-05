import pandas as pd

df = pd.read_csv('./data/billboard.csv', encoding="mac_latin2")

print(df.head(10))

# Melting
id_vars = ["year",
           "artist.inverted",
           "track",
           "time",
           "genre",
           "date.entered",
           "date.peaked"]

df = pd.melt(frame=df, id_vars=id_vars, var_name="week", value_name="rank")

# Formatting
df["week"] = df['week'].str.extract('(\d+)', expand=False).astype(int)

#Cleaning out unnecessary rows
df = df.dropna()
df["rank"] = df["rank"].astype(int)

# Create "date" columns
df['date'] = pd.to_datetime(df['date.entered']) + pd.to_timedelta(df['week'], unit='w') - pd.DateOffset(weeks=1)

df = df[["year",
         "artist.inverted",
         "track",
         "time",
         "genre",
         "week",
         "rank",
         "date"]]
df = df.sort_values(ascending=True, by=["year", "artist.inverted", "track", "week", "rank"])

# Assigning the tidy dataset to a variable for future usage
billboard = df

print('result')
print(df.head(10))

songs_columns = ["year", "artist.inverted", "track", "time", "genre"]
songs = billboard[songs_columns].drop_duplicates()
songs = songs.reset_index(drop=True)
songs["song_id"] = songs.index

print('====songs result====')
print(songs.head(10))
