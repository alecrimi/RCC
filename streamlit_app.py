import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read in the data for the two time series
#series1 = pd.read_csv("series1.csv")
#series2 = pd.read_csv("series2.csv")
x, y = [], []
x.append(0.1)
y.append(0.2)
for i in range(1, 13):
    xi = x[i-1]*(3.78-3.78*x[i-1])
    yi = y[i-1]*(3.77-3.77*y[i-1])
    x.append(xi)
    y.append(yi)

# Create a slider to control the parameter
parameter = st.sidebar.slider("Parameter", 0.0, 1.0, 0.8)
	
for i in range(13, 20001):
	xi = x[i-1]*(3.78-3.78*x[i-1])
	yi = y[i-1]*(3.77-3.77*y[i-1]-parameter*x[i-1-10])
	x.append(xi)
	y.append(yi)
series1 = x
series2 = y 

# Create the plot
plt.plot(series1.index, series1.value, label="Series 1")
plt.plot(series2.index, series2.value, label="Series 2")

# Add a legend
plt.legend()

# Show the plot
st.pyplot()
