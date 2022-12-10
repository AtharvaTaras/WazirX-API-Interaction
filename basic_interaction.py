import requests

# Public Ticker API
URL = "https://api.wazirx.com/api/v2/tickers"
PAIR = 'ethinr'

response = requests.get(URL)
data = response.json()

for each in data[PAIR]:
    print(each)

print('Buy -', (data[PAIR]['buy']))
print('Sell -', (data[PAIR]['sell']))

