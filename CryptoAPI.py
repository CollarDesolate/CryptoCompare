from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from pprint import pprint

print("Welcome to my crypto web app!")

print("Here, you can compare crypto data for any coin on CoinMarketCap")

print("Simply enter your symbols of the coins you'd like data for below, separated by a comma")

symbol1 = input("Enter your crypto symbols: ")

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=' + symbol1 + ''

parameters = {
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '53cbb7f5-d88a-4f06-8bd4-c1da594d075f',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  pprint(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  pprint(e)
