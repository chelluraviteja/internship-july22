import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\Ravi Teja\openpub_application.csv")
st.title('Pubs Location on Authority Name')
html_temp = """
    <div style="background-color:Black;padding:10px">
    <h2 style="color:white;text-align:center;"> Based on Location </h2>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
title = st.selectbox("local_authority",data["local_authority"].unique())

data = pd.read_csv(r"C:\Users\Ravi Teja\openpub_application.csv")


fetching_local_data = data.loc[data.local_authority == title,['latitude','longitude']]
st.map(fetching_local_data)

fetching_local_name = data.loc[data.local_authority == title,['name','address']].reset_index(drop=True)
st.markdown('Area Name"s and Address')
st.dataframe(fetching_local_name)