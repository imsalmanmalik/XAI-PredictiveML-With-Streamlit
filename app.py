import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
print('All packages installation successfully done!')



model = pickle.load(open('./model3.sav', 'rb'))
st.title('Property Cost Prediction')
st.sidebar.header('Properties Data')
image = Image.open('airbnb.jpg')
st.image(image, '')


def prop_data():
    latitude = st.sidebar.slider('Latitude', min_value=40.9, max_value=40.0, step=0.1, )
    longitude = st.sidebar.slider('Longitude', min_value=-73.0, max_value=-73.9, step=-0.1)
    minimum_nights = st.sidebar.slider('Minimum Nights', min_value=1, max_value=100, step=1)
    number_of_reviews = st.sidebar.slider('Number of Reviews', min_value=0, max_value=600, step=10)
    last_review = st.sidebar.slider('Last Review', min_value=1, max_value=3000, step=100)
    availability_365 = st.sidebar.slider('Availability 365', min_value=0, max_value=500, step=5)



    prop_report_data = {
        'latitude': latitude,
        'longitude': longitude,
        'minimum nights': minimum_nights,
        'number of reviews': number_of_reviews,
        'last review': last_review,
        'availability_365': availability_365
    }


    report_data = pd.DataFrame(prop_report_data, index=[0])
    return report_data


prop = prop_data()
st.header('Property Data')
st.write(prop)

price = model.predict(prop)
st.subheader('Property Cost')
st.subheader(price)
# st.subheader('$' + str(np.round(price[0], 2)))