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
	
st.write("""
# Those are the time series designed according to the parameter as in Sugihara et al.
""")	

st.sidebar.write("## Change the C parameters to change Series2 :gear:")


# Create a slider to control the parameter
C = st.sidebar.slider("C Parameter", 0.0, 1.0, 0.8)
	
for i in range(13, 20001):
	xi = x[i-1]*(3.78-3.78*x[i-1])
	yi = y[i-1]*(3.77-3.77*y[i-1]-C*x[i-1-10])
	x.append(xi)
	y.append(yi)
series1 = x
series2 = y 

# Create the plot
plt.plot(series1 , label="Series 1")
plt.plot(series2, label="Series 2")

# Add a legend
plt.legend()

# Show the plot
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
st.beta_set_page_config(page_title="Reservoir computing causality",  layout = 'wide', initial_sidebar_state = 'auto')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
