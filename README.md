# House Price Prediction Project

Welcome to the House Price Prediction Project! This application utilizes machine learning to predict the price of a house based on several key features such as the number of bedrooms, bathrooms, square footage, lot size, age of the house, proximity to the city center, and neighborhood quality.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

## Overview

The House Price Prediction Project is designed to provide an estimate of house prices using a machine learning model trained on a dataset of housing features. This Streamlit application allows users to input the characteristics of a house and receive a predicted price.

## Features

- User-friendly interface for entering house details
- Real-time prediction of house prices
- Visualization of input features
- Custom styling and animations

## Installation

To get started with this project, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/house-price-prediction.git
    cd house-price-prediction
    ```

2. **Create a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Download the dataset:**

    Ensure you have the dataset file `your_dataset.csv` in the project directory.
5. **Model Training**

    The model was trained using a comprehensive dataset of house prices with features such as the number of bedrooms, bathrooms, square footage, lot size, age of the house, proximity to 
    the city center, and neighborhood quality. The training process involved:

   1. Data preprocessing (handling missing values, encoding categorical variables, feature scaling).
   2. Splitting the dataset into training and testing sets.
   3. Training a regression model (e.g., Linear Regression, Random Forest) on the training set.
   4. Evaluating the model's performance on the test set.

   The trained model is saved as `model.pkl` and loaded in the Streamlit application for predictions.

6. **Run the Streamlit application:**

    ```sh
    streamlit run app.py
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:8501`.
2. Enter the details of the house (number of bedrooms, bathrooms, square footage, lot size, age of house, proximity to city center, neighborhood quality).
3. Click on the "Predict!" button to get the estimated house price.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for providing an easy-to-use web application framework.
- [Scikit-learn](https://scikit-learn.org/) for the machine learning tools used in this project.
- [Pandas](https://pandas.pydata.org/) for data manipulation and analysis.

---
