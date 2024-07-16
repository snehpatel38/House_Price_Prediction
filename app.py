import streamlit as st
import bz2file as bz2
import pickle
import numpy as np

# Define decompression function
def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data

# Load the compressed model
model = decompress_pickle('model.pbz2')

st.title('House Price Prediction Project')

st.divider()

st.write("This app uses machine learning to predict house prices based on various features of the house. Enter the details below and click 'Predict!'")

st.divider()

# Inputs for the features
bedrooms = st.number_input('Number of bedrooms', min_value=0, value=0)
bathrooms = st.number_input('Number of bathrooms', min_value=0, value=0)
square_footage = st.number_input('Square footage', min_value=0, value=2000)
lot_size = st.number_input('Lot size', min_value=0, value=0)
age_of_house = st.number_input('Age of house', min_value=0, value=0)
proximity_to_city_center = st.number_input('Proximity to city center', min_value=0, value=0)
neighborhood_quality = st.number_input('Neighborhood quality', min_value=0, value=0)

st.divider()

# Create the input array for prediction
X = [[bedrooms, bathrooms, square_footage, lot_size, age_of_house, proximity_to_city_center, neighborhood_quality]]

predict_button = st.button('Predict!')

if predict_button:
    st.balloons()
    
    X_array = np.array(X)
    prediction = model.predict(X_array)
    
    st.write(f'The predicted price of the house is ${np.round(prediction[0], 2)}')
