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

# Define icons and names for sidebar navigation
sidebar_items = {
    'About Project': {'icon': '🏠', 'name': 'Project'},
    'About Internship': {'icon': '👩‍🎓', 'name': 'About Internship'},
    'About Me': {'icon': '🧑‍💻', 'name': 'About Me'}
}

# Page title and sidebar sections
#st.title('House Price Prediction Project')

st.sidebar.title('Navigation')

# Sidebar navigation with icons and names
nav_selection = st.sidebar.radio('',
    list(sidebar_items.keys()),
    format_func=lambda x: f"{sidebar_items[x]['icon']} {sidebar_items[x]['name']}")

# Different sections
if nav_selection == 'About Project':
    st.header(f"{sidebar_items['About Project']['icon']} {sidebar_items['About Project']['name']}")
    st.markdown("""
    Explain briefly what your house price prediction project aims to achieve.
    """)

    # Styling and input fields for prediction
    st.subheader('House Price Prediction')
    
    st.write("Enter the details below and click 'Predict!'")
    
    # Inputs for the features
    bedrooms = st.number_input('Number of Bedrooms', min_value=0, value=0)
    bathrooms = st.number_input('Number of Bathrooms', min_value=0, value=0)
    square_footage = st.number_input('Square Footage (800-3499)', min_value=0, value=2000)
    #lot_size = st.number_input('Lot Size', min_value=0, value=0)
    age_of_house = st.number_input('Age of House', min_value=0, value=0)
    proximity_to_city_center = st.number_input('Proximity to City Center (miles)', min_value=0, value=0)
    neighborhood_quality = st.number_input('Neighborhood Quality (1-10)', min_value=0, value=0)
    
    # Predict button
    predict_button = st.button('Predict!')
    if predict_button:
        st.balloons()  # Fun element to show prediction

        # Create the input array for prediction
        X = [[bedrooms, bathrooms, square_footage, age_of_house, proximity_to_city_center, neighborhood_quality]]
        X_array = np.array(X)

        # Prediction
        prediction_usd = model.predict(X_array)[0]
        prediction_inr = prediction_usd * 83

        st.write(f'The predicted price of the house is ₹ {np.round(prediction_inr, 2)} INR')

elif nav_selection == 'About Internship':
    st.header(f"{sidebar_items['About Internship']['icon']} {sidebar_items['About Internship']['name']}")
    st.markdown("""
    - Completed a 15-day internship focused on data analysis and machine learning at INFOLABZ IT SERVICES PVT LTD.
    - Gained practical experience in data fetching from APIs, including Bitcoin and Covid APIs.
    - Applied data analysis techniques using Pandas, including storing and reading data from Excel.
    - Developed skills in data visualization with various graphs (bargraphs, linegraphs, pie charts, scatter graphs).
    - Implemented machine learning algorithms such as Linear Regression and Multiple Linear Regression.
    - Successfully applied learned concepts to real-world project implementations.
    """)

elif nav_selection == 'About Me':
    st.header(f"{sidebar_items['About Me']['icon']} {sidebar_items['About Me']['name']}")
    st.divider()
    st.markdown("""
    Hello! I'm Sneh Patel, currently pursuing Computer Engineering at Saffrony Institute Of Technology. 
    """)
