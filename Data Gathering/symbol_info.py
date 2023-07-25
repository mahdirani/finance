import requests
import json

url = "https://www.bitstamp.net/api/v2/trading-pairs-info/"
get = requests.get(url).json()
# get the data from bitstamp API endpoint for trading pairs information
#in JSON format and store it into a variable called 'data'
#using .json() method of response object

pairs_name = []
for info in get:
    pairs_name.append(info["name"])
    pairs_name.append("\n")

with open("pairs_name.csv", "w") as f:
    f.writelines(pairs_name)

