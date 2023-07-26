#!/usr/bin/env python3

import json
import requests
import datetime
import pandas as pd

currency_pair = "eurusd"
url = f"https://www.bitstamp.net/api/v2/ohlc/{currency_pair}/"

start = "2023-01-01"
end = "2023-07-25"
timeframe = 300

dates = pd.date_range(start, end, freq="12H")
dates = [ int(x.value/10**9) for x in list(dates)]
print(dates)

master_data = []

for first, last in zip(dates, dates[1:]):
    print(first,last)
    params = {
            "step":timeframe,
            "limit":1000,
            "start":first,
            "end":last,
            }

    data = requests.get(url, params=params)

    data = data.json()["data"]["ohlc"]

    master_data += data 

df = pd.DataFrame(master_data)
df = df.drop_duplicates()

df["timestamp"] = df["timestamp"].astype(int)
df = df.sort_values(by="timestamp")

df = df[ df["timestamp"] >= dates[0] ]
df = df[ df["timestamp"] < dates[-1] ]

print(df)

df.to_csv(f"{currency_pair}-{timeframe}|||{start}-{end}.csv", index=False)
