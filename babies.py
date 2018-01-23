import pandas as pd
import datetime
import re
import glob

df = pd.read_csv('./data/weather-raw.csv')
print(df)


def extract_year(string):
    match = re.match(".+(\d{4})", string)
    if match != None: return match.group(1)


path = './data'


allFiles = glob.glob(path + "/201*-baby-names-illinois.csv")
frame = pd.DataFrame()
df_list= []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    df.columns = map(str.lower, df.columns)
    df["year"] = extract_year(file_)
    df_list.append(df)

df = pd.concat(df_list)
print('')
print(df.head(5))