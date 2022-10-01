import pandas as pd
import streamlit as st
from pickle import load
import os
import pickle

# loading the data using the address from os

import os
filepath = "/Users/Ravi Teja/OneDrive/Desktop/project1/models/rfr_model.pkl"

if os.path.exists(filepath):
    file = open('/Users/Ravi Teja/OneDrive/Desktop/project1/models/rfr_model.pkl', 'rb')
    codedata = pickle.load(file)
    file.close()
else:
    print("File not present at desired location")



# import os
# dirname = os.path.dirname("__file__")
# filename = os.path.join(dirname, "C:/Users/Ravi Teja/OneDrive/Desktop/project1/models/lr_model.pkl")

rfr_model = load(open(filepath,'rb'))

# Define the prediction function
def predict(carat, cut, color, clarity, depth, table, x, y, z):
    #Predicting the price of the carat
    if cut == 'Fair':
        cut = 0
    elif cut == 'Good':
        cut = 1
    elif cut == 'Very Good':
        cut = 2
    elif cut == 'Premium':
        cut = 3
    elif cut == 'Ideal':
        cut = 4

    if color == 'J':
        color = 0
    elif color == 'I':
        color = 1
    elif color == 'H':
        color = 2
    elif color == 'G':
        color = 3
    elif color == 'F':
        color = 4
    elif color == 'E':
        color = 5
    elif color == 'D':
        color = 6
    
    if clarity == 'I1':
        clarity = 0
    elif clarity == 'SI2':
        clarity = 1
    elif clarity == 'SI1':
        clarity = 2
    elif clarity == 'VS2':
        clarity = 3
    elif clarity == 'VS1':
        clarity = 4
    elif clarity == 'VVS2':
        clarity = 5
    elif clarity == 'VVS1':
        clarity = 6
    elif clarity == 'IF':
        clarity = 7
    

    prediction = rfr_model.predict(pd.DataFrame([[carat, cut, color, clarity, depth, table, x, y, z]], columns=['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']))
    return prediction

st.title("Diamond Price Prediction")
html_temp = """
<div style ="background-color:Tomato;padding:13px">
<h1 style ="color:white;text-align:center;">Diamond Price Prediction</h1>
</div>
    """    
st.markdown(html_temp, unsafe_allow_html=True)

carat = st.text_input("Carat")
cut = st.text_input("Cut")
color = st.text_input("Color")
clarity = st.text_input("Clarity")
depth = st.text_input("Depth")
table = st.text_input("table")
x = st.text_input("X")
y = st.text_input("Y")
z = st.text_input("Z")
   

if st.button('Predict Price'):
    price = predict(carat, cut, color, clarity, depth, table, x, y, z)
    st.success(f'The predicted price of the diamond is {price[0]:.2f} INR')
