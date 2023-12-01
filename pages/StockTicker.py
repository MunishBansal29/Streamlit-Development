from time import sleep
import streamlit as st
import plotly.express as px
import yfinance as finance
import time
# import matplotlib.pyplot as plt
from streamlit_autorefresh import st_autorefresh
import streamlit.components.v1 as components



st.title("Real-time Google Stock Prices")

# # Define the ticker symbol for Apple
# ticker_symbol = 'GOOGL'

# # Get the data of the stock
# google_stock = yf.Ticker(ticker_symbol)

# # Create a matplotlib figure
# fig, ax = plt.subplots()

# # Use st.pyplot to display the plot
# plot = st.pyplot(fig)
   
count = st_autorefresh(interval=1000, limit=100, key="fizzbuzzcounter")
# The function returns a counter for number of refreshes. This allows the
# ability to make special requests at different intervals based on the count
if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz")
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"Count: {count}")


st.write("Current time - ", time.time()) #This also changes every second, and proves that st_autorefresh() refreshes the entire page, not a single component/part of it.


stock_list = ['RELIANCE.NS', 'TATAMOTORS.NS', 'TCS.NS', 'INFY.NS', 'WIPRO.NS']
col1 = st.empty()

with col1.container():
    for index, val in enumerate(stock_list):
            stock = finance.Ticker(val)
            todays_data = stock.history(period='1d')
            price = todays_data['Close'][0]
            # price = stock.info['regularMarketPrice']
            # st.write(stock.info)
            st.write(stock.info["longName"], ":", round(price, 1))


def get_ticker(name):
    company = finance.Ticker(name)  # google
    return company
 
 
 
company1 = get_ticker("GOOGL")
company2 = get_ticker("MSFT")
 
# fetches the data: Open, Close, High, Low and Volume
google = finance.download("GOOGL", start="2023-10-01", end="2023-11-01")
microsoft = finance.download("MSFT", start="2023-10-01", end="2023-11-01")
 
# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
data1 = company1.history(period="3mo")
data2 = company2.history(period="3mo")
 
# markdown syntax
st.write("""
### Google
""")
 
# detailed summary on Google
st.write(company1.info['longBusinessSummary'])  
st.write(google)
 
# plots the graph
st.line_chart(data1.values)  
 
st.write("""### Microsoft """)
st.write(company2.info['longBusinessSummary'], "\n", microsoft)
st.line_chart(data2.values)
