import requests
import json
import pandas as pd
import mplfinance as mpl

url = 'https://www.mexc.com/open/api/v2/market/kline?interval=1m&limit=1000&symbol=AES_USDT'
response = requests.get(url)
responseBody = response.text
responseBodyJson = json.loads(responseBody)

candlesData = responseBodyJson["data"]
formattedCandlesData = []
for candle in candlesData:
    formattedCandle = {
        'time': candle[0],
        'open': float(candle[1]),
        'close': float(candle[2]),
        'high': float(candle[3]),
        'low': float(candle[4])
    }
    formattedCandlesData.append(formattedCandle)

df = pd.json_normalize(formattedCandlesData)
df.time = pd.to_datetime(df.time, unit='s')
df = df.set_index("time")

# szukanie dopasowania
pattern = df.iloc[-10:]  # ostatnie 10 świec
window_size = 10  # rozmiar okna do porównania
tolerance = 0.05  # tolerancja na dopasowanie

for i in range(len(df) - window_size):
    window = df.iloc[i:i+window_size]  # okno danych do porównania
    if (window['open'].std() < tolerance * pattern['open'].std() and
        window['close'].std() < tolerance * pattern['close'].std()):
        matching_index = i
        break

matching_window = df.iloc[matching_index:matching_index+window_size]
mpl.plot(matching_window, type='candle', style='yahoo')
mpl.show()
mpl.plot(pattern, type='candle', style='yahoo')
mpl.show()



