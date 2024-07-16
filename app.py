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
        prediction = model.predict(X_array)
        st.write(f'The predicted price of the house is ${np.round(prediction[0], 2)}')

elif nav_selection == 'About Internship':
    st.header(f"{sidebar_items['About Internship']['icon']} {sidebar_items['About Internship']['name']}")
    st.divider()
    st.markdown("""
    I recently completed a focused 15-day internship at INFOLABZ IT SERVICES PVT LTD in the field of data analysis and machine learning. Throughout the internship, I engaged deeply with various aspects of these fields, gaining hands-on experience in practical applications such as:

    -Introduction to Machine Learning and its fundamentals.
    -Fetching and analyzing data from APIs, including Bitcoin and Covid APIs.
    -Utilizing Pandas for data manipulation and analysis, including storing data to Excel and reading from Excel files.
    -Data visualization techniques using tools like Excel and Python for creating graphs (bargraphs, linegraphs, pie charts, scatter graphs).
    -Implementation of machine learning algorithms, starting with Linear Regression and progressing to Multiple Linear Regression.
    -Project work involving real-world datasets and applying learned techniques for data analysis and prediction."
    """)

elif nav_selection == 'About Me':
    st.header(f"{sidebar_items['About Me']['icon']} {sidebar_items['About Me']['name']}")
    st.divider()
    st.markdown("""
    Hello! I'm Sneh Patel, currently pursuing Computer Engineering at Saffrony Institute Of Technology. 
    """)
