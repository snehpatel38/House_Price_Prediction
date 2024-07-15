import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load('model.pkl')

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        .title {
            font-size: 2.5em;
            color: #4CAF50;
            text-align: center;
            margin-bottom: 0.5em;
        }
        .divider {
            border-bottom: 1px solid #ccc;
            margin: 20px 0;
        }
        .section-header {
            font-size: 1.5em;
            color: #333;
            margin-top: 1em;
        }
        .button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
            color: #777;
        }
        .tooltip {
            position: relative;
            display: inline-block;
            cursor: pointer;
        }
        .tooltip .tooltiptext {
            visibility: hidden;
            width: 120px;
            background-color: #6c757d;
            color: #fff;
            text-align: center;
            border-radius: 6px;
            padding: 5px;
            position: absolute;
            z-index: 1;
            bottom: 100%;
            left: 50%;
            margin-left: -60px;
            opacity: 0;
            transition: opacity 0.3s;
        }
        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">House Price Prediction Project</div>', unsafe_allow_html=True)

# Introduction Section
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.subheader('Introduction')
st.write("""
    Welcome to the House Price Prediction Project! This application utilizes machine learning to predict the price of a house based on several key features.
    Please enter the details of the house in the fields below and click on the 'Predict!' button to get the estimated price.
""")
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# How the Model Works Section
st.subheader('How the Model Works')
st.write("""
    The model has been trained on a comprehensive dataset of house prices, considering various factors such as:
    - Number of bedrooms
    - Number of bathrooms
    - Square footage
    - Lot size
    - Age of the house
    - Proximity to the city center
    - Neighborhood quality

    By analyzing these features, the model can provide an accurate prediction of house prices.
""")
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Input Section
st.subheader('Enter House Details')
bedrooms = st.number_input('Number of Bedrooms', min_value=0, value=0, help='Enter the number of bedrooms in the house.')
bathrooms = st.number_input('Number of Bathrooms', min_value=0, value=0, help='Enter the number of bathrooms in the house.')
square_footage = st.number_input('Square Footage', min_value=0, value=2000, help='Enter the total square footage of the house between 800 to 3499.')
#lot_size = st.number_input('Lot Size', min_value=0, value=0, help='Enter the lot size of the house.')
age_of_house = st.number_input('Age of House', min_value=0, value=0, help='Enter the age of the house in years.')
proximity_to_city_center = st.number_input('Proximity to City Center', min_value=0, value=0, help='Enter the distance to the city center in miles.')
neighborhood_quality = st.number_input('Neighborhood Quality', min_value=0, value=0, help='Rate the neighborhood quality on a scale of 0 to 10.')

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Prediction Section
st.subheader('Prediction')
X = [[bedrooms, bathrooms, square_footage, age_of_house, proximity_to_city_center, neighborhood_quality]]

predictbutton = st.button('Predict!', key='predict_button')

if predictbutton:
    st.balloons()
    X_array = np.array(X)
    prediction = model.predict(X)
    st.success(f'The predicted price of the house is ${np.round(prediction[0], 2)}')

st.markdown("""
    <style>
        #predict_button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 12px;
        }
        #predict_button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="footer">Developed by Sneh.</div>', unsafe_allow_html=True)
