import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcome to Open pub application")
html_temp = """
    <div style="background-color:Black;padding:10px">
    <h2 style="color:PINK;text-align:center;"> PUB APPLICATION </h2>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
data = pd.read_csv(r"C:\Users\Ravi Teja\openpub_application.csv")
st.dataframe(data)
st.header('Shape of Data')
st.dataframe(data.shape)
st.text('There is 50,563 active pubs in United Kingdom')