import streamlit as st
import bz2
import pickle
import numpy as np

# Define decompression function
def decompress_pickle(file):
    with bz2.BZ2File(file, 'rb') as f:
        data = pickle.load(f)
    return data

# Load the compressed model
model = decompress_pickle('model.pbz2')

st.title('House Price Prediction Project')

st.divider()

st.write("This app uses machine learning to predict house prices based on various features of the house. Enter the details below and click 'Predict!'")

st.divider()

# Inputs for the features
bedrooms = st.number_input('num_bedrooms', min_value=0, value=0)
bathrooms = st.number_input('num_bathrooms', min_value=0, value=0)
square_footage = st.number_input('square_footage', min_value=0, value=2000)
#lot_size = st.number_input('Lot size', min_value=0, value=0)
age_of_house = st.number_input('age_of_house', min_value=0, value=0)
proximity_to_city_center = st.number_input('proximity_to_city_center', min_value=0, value=0)
neighborhood_quality = st.number_input('neighborhood_quality', min_value=0, value=0)

st.divider()

# Create the input array for prediction
X = [[bedrooms, bathrooms, square_footage, age_of_house, proximity_to_city_center, neighborhood_quality]]

predict_button = st.button('Predict!')

if predict_button:
    st.balloons()

    # Convert the input to a numpy array
    X_array = np.array(X)

    # Debugging: Print out the shape of the input and the expected number of features
    st.write(f"Input shape: {X_array.shape}")
    st.write(f"Expected number of features: {model.n_features_in_}")

    # Ensure the input is in the correct shape
    try:
        prediction = model.predict(X_array)
        st.write(f'The predicted price of the house is ${np.round(prediction[0], 2)}')
    except ValueError as e:
        st.error(f"Error during prediction: {e}")
