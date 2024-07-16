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

# Define icons for sidebar navigation
sidebar_icons = {
    'About Project': '🏠',
    'About Internship': '👩‍🎓',
    'About Me': '🧑‍💻'
}

# Page title and sidebar sections
st.title('House Price Prediction Project')

st.sidebar.title('Navigation')

# Sidebar navigation with icons
nav_selection = st.sidebar.radio('',
    list(sidebar_icons.keys()),
    format_func=lambda x: sidebar_icons[x])

# Different sections
if nav_selection == 'About Project':
    st.header('About the Project')
    st.markdown("""
    Explain briefly what your house price prediction project aims to achieve.
    """)

elif nav_selection == 'About Internship':
    st.header('About the Internship')
    st.markdown("""
    Describe your internship experience, what you've learned, and how it relates to this project.
    """)

elif nav_selection == 'About Me':
    st.header('About Me')
    st.markdown("""
    Introduce yourself, your background, and your interests related to this project.
    """)

# Styling and input fields for prediction
st.subheader('House Price Prediction')
st.write("Enter the details below and click 'Predict!'")

# Inputs for the features
bedrooms = st.number_input('Number of Bedrooms', min_value=0, value=0)
bathrooms = st.number_input('Number of Bathrooms', min_value=0, value=0)
square_footage = st.number_input('Square Footage', min_value=0, value=2000)
lot_size = st.number_input('Lot Size', min_value=0, value=0)
age_of_house = st.number_input('Age of House', min_value=0, value=0)
proximity_to_city_center = st.number_input('Proximity to City Center (miles)', min_value=0, value=0)
neighborhood_quality = st.number_input('Neighborhood Quality (1-10)', min_value=0, value=0)

# Prediction button
st.subheader('Predict House Price')
predict_button = st.button('Predict!')

if predict_button:
    st.balloons()  # Fun element to show prediction

    # Create the input array for prediction
    X = [[bedrooms, bathrooms, square_footage, lot_size, age_of_house, proximity_to_city_center, neighborhood_quality]]
    X_array = np.array(X)

    # Prediction
    prediction = model.predict(X_array)
    st.write(f'The predicted price of the house is ${np.round(prediction[0], 2)}')
