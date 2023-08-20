# House Price Prediction Project

Welcome to my House Price Prediction project! In this repository, I've tackled the challenge of predicting house prices using advanced regression techniques. The project was developed as part of the Kaggle competition ["House Price Prediction: Advanced Regression Techniques"](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data).

## Overview

The goal of this project was to accurately predict house prices based on a rich dataset of features, including numerical, categorical, and temporal attributes. Leveraging data preprocessing, feature engineering, and model optimization, I aimed to create robust regression models that can provide accurate estimates of house sale prices.


## Key Features

- Data preprocessing to handle missing values and categorical variables.
- Exploratory data analysis to gain insights into the dataset.
- Feature engineering to extract valuable information from the raw data.
- Implementation of advanced regression techniques for accurate predictions.
- Model evaluation using cross-validation and performance metrics.

## Repository Contents

- `data/`: This folder contains the dataset provided by Kaggle, including both the training and test sets.
- `Code.ipynb`: Jupyter notebooks detailing the step-by-step process of data analysis, feature engineering, and model development.
- `README.md`: You're reading it! An overview of the project, its contents, and how to use it.
- `flask-app/`: Contains the Flask API for making single predictions.
    - `main.py`: Run this script to start the Flask app.
    - `app/`: Subdirectory containing the API logic.
        - `app.py`: API routes and responses.
        - `service.py`: Helper functions for data processing.



## Flask API for Single Predictions

The `flask-app` directory contains a Flask API that allows you to make single predictions using the trained model. Here's how you can run the API:

1. Install the required dependencies by running: `pip install -r requirements.txt`
2. Navigate to the `flask-app` directory: `cd flask-app`
3. Run the Flask app by executing `python main.py`:


The API will start running locally on `http://localhost:5000`.

4. To make a single prediction, you can send a POST request to the `/api/v1/single/prediction` endpoint with JSON data containing the required features for prediction.

Example using `curl`:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"feature1": value1, "feature2": value2, ...}' http://localhost:5000/api/v1/single/prediction
````
## Dependencies

- Python 3.x
- Jupyter Notebook
- Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, etc. (See requirements.txt for details)

## Note

This project is for showcasing my data science skills in 2021 (Of course now I am much better 😊). It was originally created for the Kaggle competition and is shared here to highlight my expertise in data preprocessing, feature engineering, and regression modeling.

Feel free to explore the notebooks and reach out if you have any questions or suggestions!

---

