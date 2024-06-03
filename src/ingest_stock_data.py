from stock_price_prediction.utils.db_util import DBConnection
from stock_price_prediction.utils.api_util import APIUtil
from typing import Any, Dict, List, Optional
from datetime import datetime, timedelta

import psycopg2.extras as p

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit app
st.title("Stock Price Trend for the Last Month")

# Input for stock symbol and API key
symbol = st.text_input("Enter stock symbol (e.g., AAPL):")
api_key = st.text_input("Enter your Alpha Vantage API key:", type="password")

if symbol and api_key:
    data = fetch_stock_data(symbol, api_key)
    if data:
        df = process_stock_data(data)
        one_month_ago = datetime.now() - timedelta(days=30)
        df_last_month = df[df['Date'] >= one_month_ago]

        # Plotting
        fig, ax = plt.subplots()
        ax.plot(df_last_month['Date'], df_last_month['Close Price'], marker='o')
        ax.set_title(f"Stock Price Trend for {symbol} (Last 1 Month)")
        ax.set_xlabel("Date")
        ax.set_ylabel("Close Price (USD)")
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Display the plot
        st.pyplot(fig)

        # Display the data
        st.write("Stock Price Data (Last 1 Month):")
        st.dataframe(df_last_month)

def _get_exchange_insert_query() -> str:
    return '''
    INSERT INTO stocks.daily_price (
        id,
        name,
        ticker,
        created_timestamp,
        last_updated_timestamp
    )
    VALUES (
        %(id)s,
        %(name)s,
        %(ticker)s,
        %(created_timestamp)s,
        %(last_updated_timestamp)s
    );
    '''

def ingest_data_into_db() -> None:
	connetion cls = DBConnection()
    with connetion.cursor() as curr:
        p.execute_batch(curr, _get_exchange_insert_query(), data)	

def fetch_data() -> List[Dict[str, str]]:
	apicls = APIUtil()
	data = apicls.make_api_call()
	return data

def run() -> None:
	data = fetch_date()
	process_and_ingest_data(data)

if __name__ == '__main__':
	run()
