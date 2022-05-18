import os
from binance.client import Client
api_key = os.environ.get('BINANCE_API_KEY')
api_secret = os.environ.get('BINANCE_API_SECRET')
client = Client(api_key, api_secret)
client.API_URL = 'https://api.binance.com/api'

def get_sybol_price(symbol_list):
    text = ''
    for  symbol in symbol_list:
        symbol =symbol.upper()
        if 'USDT' not in symbol:
            symbol+='USDT'
        symbol_data = client.get_symbol_ticker(symbol=symbol)
        text += f"{symbol}:{float(symbol_data['price']):0.4f}\n"

    return text