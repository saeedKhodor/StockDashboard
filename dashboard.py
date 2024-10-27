import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Page Title
st.title("Stock Analysis Dashboard")

# Ticker Selection
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL)", "AAPL")

# Date Selection
start_date = st.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("today"))

# Fetch Data Button
if st.button("Fetch Data"):
    data = yf.download(ticker, start=start_date, end=end_date)
    if not data.empty:
        st.write(f"Displaying data for {ticker} from {start_date} to {end_date}")
        st.write(data.tail())  # Show the latest entries
    else:
        st.write("No data found. Please check the ticker and date range.")


    # Plot Closing Prices
    if not data.empty:
        st.subheader(f"{ticker} Closing Price Over Time")
        st.line_chart(data['Close'])

        # Additional plots or analysis
        st.subheader("Moving Average")
        data['Moving Avg'] = data['Close'].rolling(window=20).mean()
        st.line_chart(data[['Close', 'Moving Avg']])
