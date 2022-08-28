import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Nearest Pub"
)

data = pd.read_csv(r"C:\Users\Ravi Teja\openpub_application.csv")
st.title('Nearest Pubs base on Latitude and Longitude.')
html_temp = """
    <div style="background-color:Black;padding:10px">
    <h2 style="color:white;text-align:center;"> Nearest Pubs </h2>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

lat = st.selectbox('latitude',data["latitude"].unique())
lon = st.selectbox('longitude',data["longitude"].unique())
button = st.button("Submit Local Authority")
data_new = data[['latitude', 'longitude']]
new_points = np.array([lat, lon])

# Calculate distance between new_points and all points in df_new using Euclidean distance 
distances = np.sqrt(np.sum((new_points - data_new)**2, axis = 1))


# sort the array using arg partition and keep only 5 elements
n = 5
min_indices = np.argpartition(distances,n-1)[:n]
if button:
    st.text("The location corresponding to below minimum distances : ")
    st.dataframe(data.iloc[min_indices])
    st.text("The minimum distances are:")
    st.dataframe(distances.head(5))
    st.map(data.iloc[min_indices])





