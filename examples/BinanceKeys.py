"""
The BinanceKeys.py Program is for keeping track of Binance Keys for use with RoibalBot.py and
save_historical_data_Roibal.py
"""
api_key_file = open('api_key', 'r')
api_secret_file = open('api_secret', 'r')

BinanceKey1 = {}
BinanceKey1['api_key'] = api_key_file.read()
BinanceKey1['api_secret'] = api_secret_file.read()
