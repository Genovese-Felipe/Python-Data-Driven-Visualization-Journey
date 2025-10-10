"""Handles the training of the predictive model for the V3 dashboard.

This script contains the logic for training the linear regression model
that predicts annual energy savings based on installation cost, number of
devices, and customer satisfaction. It also calculates the feature
importance for use in the dashboard's predictive visualization.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def train_energy_savings_model(df):
    """Trains a linear regression model to predict energy savings.

    This function takes a DataFrame of smart home installation data,
    trains a linear regression model to predict 'Annual_Energy_Savings',
    and calculates the importance of each feature.

    Args:
        df (pd.DataFrame): The DataFrame containing the smart home
                           installation data.

    Returns:
        tuple: A tuple containing:
            - LinearRegression: The trained linear regression model.
            - pd.DataFrame: A DataFrame with the calculated feature
                            importance.
    """
    X = df[['Installation_Cost', 'Number_of_Devices', 'Customer_Satisfaction']]
    y = df['Annual_Energy_Savings']

    model = LinearRegression()
    model.fit(X, y)

    feature_importance = pd.DataFrame({
        'feature': ['Installation Cost', 'Number of Devices', 'Customer Satisfaction'],
        'importance': np.abs(model.coef_)
    }).sort_values('importance', ascending=False)

    return model, feature_importance