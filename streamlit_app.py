import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pyrcn.echo_state_network import ESNRegressor

# Read in the data for the two time series
#series1 = pd.read_csv("series1.csv")
#series2 = pd.read_csv("series2.csv")
x, y = [], []
x.append(0.1)
y.append(0.2)
nochangerange = 13
for i in range(1, nochangerange):
    xi = x[i-1]*(3.78-3.78*x[i-1])
    yi = y[i-1]*(3.77-3.77*y[i-1])
    x.append(xi)
    y.append(yi)
	
st.title("Reservoir Computing Causality Demo")	


st.sidebar.write("## Change the C parameters to change Series2 as in Sugihara et al. :gear:")


# Create a slider to control the parameter
C = st.sidebar.slider("C Parameter", 0.0, 0.85, 0.8)
	
for i in range(nochangerange, 20001):
	xi = x[i-1]*(3.78-3.78*x[i-1])
	yi = y[i-1]*(3.77-3.77*y[i-1]-C*x[i-1-10])
	x.append(xi)
	y.append(yi)
series1 = x
series2 = y 

# Create the plot
st.markdown(" First 50 time points of the 2 demo series")	
plt.plot(series1[:50] , label="Series 1")
plt.plot(series2[:50], label="Series 2")

# Add a legend
plt.legend()

# Show the plot
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()


from pyrcn.echo_state_network import ESNRegressor
import numpy as np
# Split data in train and test
X_train = np.array(x[:15000]).reshape(-1, 1)
y_train = np.array(y[:15000])
X_test = np.array(x[15000:]).reshape(-1, 1)
y_test = np.array(y[15000:])

# Initialise the regressor
reg = ESNRegressor()
# Fit the regresor
reg.fit(X=X_train, y=y_train)
# Predict Ys
y_pred = reg.predict(X_test)

# Store in a dataframe all but the first twenty time steps
import pandas as pd
out_df = pd.DataFrame(columns=['y ground-truth', 'y predicted'])
out_df['y_test'] = y_test[20:]
out_df['y_pred'] = y_pred[20:]
# Calculate Pearson's coefficient
st.markdown("The Pearson correlation of the predicted series with the ground truth in crossvalidation manner was: ")
peacorr = np.corrcoef(y_test[20:], y_pred[20:])
st.markdown(peacorr[0,1])

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
