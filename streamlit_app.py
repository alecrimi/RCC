import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read in the data for the two time series
series1 = pd.read_csv("series1.csv")
series2 = pd.read_csv("series2.csv")

# Create the plot
plt.plot(series1.index, series1.value, label="Series 1")
plt.plot(series2.index, series2.value, label="Series 2")

# Add a legend
plt.legend()

# Show the plot
st.pyplot()
