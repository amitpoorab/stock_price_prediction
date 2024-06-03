import requests
import logging

class APIUtil:
	def __init__(self):
		pass

def make_api_call() -> str :    
    # Base URL for the Alpha Vantage API
	base_url = 'https://www.alphavantage.co/query'
	params = {
    'function': 'TIME_SERIES_DAILY',  
    'symbol': 'AAPL',  # TODO we need get symbol dynamically
    'apikey': os.getenv('API_kEY', '')
	}

    try:
        r = requests.get(base_url)
    except requests.ConnectionError as ce:
        logging.error(f"There was an error with the request, {ce}")
        sys.exit(1)
    return r.json().get('data', [])
