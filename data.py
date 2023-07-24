#!/usr/bin/env python3

import json
import requests
import datetime
import pandas as pd

currency_pair = "eurusd"
url = f"https://www.bitstamp.net/api/v2/ohlc/{currency_pair}/"

params = {
        "step":300,
        "limit":1000,
        }

data = requests.get(url, params=params)

print(data.json())