# ACC102 Mini Assignment - Track4
# Interactive Financial Data Analysis Tool (100% Local, No External Dependencies)
# Data Source: Simulated MSFT Stock Data
# Student ID: 2470452
# Student Name: Zhuowei.Li

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Page setup
st.title("Interactive Stock Price Analysis Tool")
st.subheader("A Python Data Product for ACC102")
st.write("User: Investors and finance students")

# 100% Local data generation (no files, no internet)
@st.cache_data
def generate_stock_data():
    # Create date range from 2023-01-01 to 2026-01-01
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2026, 1, 1)
    date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days)]
    
    # Generate realistic stock price trend
    np.random.seed(42)
    base_price = 240
    daily_returns = np.random.normal(0.0005, 0.015, len(date_range))
    price_series = base_price * (1 + daily_returns).cumprod()
    
    # Create DataFrame
    data = pd.DataFrame({
        'Date': date_range,
        'Open': price_series * np.random.uniform(0.998, 1.002, len(date_range)),
        'High': price_series * np.random.uniform(1.001, 1.005, len(date_range)),
        'Low': price_series * np.random.uniform(0.995, 0.999, len(date_range)),
        'Close': price_series,
        'Adj Close': price_series,
        'Volume': np.random.randint(10000000, 50000000, len(date_range))
    })
    data.set_index('Date', inplace=True)
    return data

# Load generated data
data = generate_stock_data()

# Show raw data
st.subheader("Raw Simulated Data")
st.dataframe(data.tail(10))

# Data cleaning
data_clean = data.dropna()
st.success("Data cleaning completed: Missing values removed")

# Analysis
st.subheader("Key Metrics")
st.write("Highest Price:", round(data_clean["Close"].max(), 2))
st.write("Lowest Price:", round(data_clean["Close"].min(), 2))
st.write("Average Price:", round(data_clean["Close"].mean(), 2))

# Visualization
st.subheader("Closing Price Trend")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(data_clean["Close"], label="Close Price", color="blue", linewidth=1.5)
ax.set_title("Microsoft (MSFT) Simulated Stock Price Trend (2023-2026)")
ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
ax.legend()
st.pyplot(fig)

st.write("This tool supports fast financial analysis with Python.")