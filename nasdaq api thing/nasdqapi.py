import requests

url = 'https://dataondemand.nasdaq.com/api/v1/analytics/async/summarizedTrades'

payload = { "start": "2018-08-27T10:00:00.000Z", "end": "2018-08-27T11:00:00.000Z" , "market_centers": ["string"], "symbols": ["AAPL"], "trade_period": 0, "trade_precision": "SECOND" }
headers = {'accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer __token__'}

response = requests.request('POST', url, json=payload, headers=headers)

print(response.text)