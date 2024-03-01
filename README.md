# House-Price-Prediction-Model
This is a machine learning project for predicting prices of real estate properties using the Bengaluru dataset.
Bengaluru House Price Prediction Model
This repo contains a machine learning model to predict Bengaluru house prices based on features like square footage, bedrooms, location etc.

Files
Bengaluru_House_Data.csv: Raw housing dataset
cleaned_data.csv: Preprocessed data used for model training
house_price.ipynb: Jupyter notebook containing data preparation, model training, evaluation and price predictions
requirements.txt: Python package dependencies
Data Cleaning and Preparation
The raw housing data (Bengaluru_House_Data.csv) was cleaned by:

Handling missing values
Removing outliers
Encoding categorical columns
Splitting into train and test sets
The cleaned data was saved in cleaned_data.csv.

Model Training and Evaluation
house_price.ipynb trains and evaluates a regression model for house price prediction.

The following models were trained and evaluated:

Linear regression (no regularization)
Lasso regression
Ridge regression
Their performance was:
