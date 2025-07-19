# Prepare Data for Complex Dashboard (Simulated Dataset)

import pandas as pd
import numpy as np

# Simulate a dataset for Smart Home Installation Analytics
# Levels: Region, City, Installation Type
# Metrics: Installation Cost, Energy Savings (Annual), Number of Devices, Customer Satisfaction Score, Latitude, Longitude

data = {
    'Region': ['North', 'North', 'North', 'South', 'South', 'South', 'East', 'East', 'West', 'West'],
    'City': ['Seattle', 'Seattle', 'Portland', 'Austin', 'Dallas', 'Houston', 'New York', 'Boston', 'San Francisco', 'Los Angeles'],
    'Installation_Type': ['Solar Panels', 'Smart Thermostat', 'Solar Panels', 'Smart Thermostat', 'Security System', 'Solar Panels', 'Smart Thermostat', 'Security System', 'Solar Panels', 'Smart Thermostat'],
    'Installation_Cost': np.random.randint(2000, 25000, 10),
    'Annual_Energy_Savings': np.random.randint(500, 3000, 10),
    'Number_of_Devices': np.random.randint(2, 15, 10),
    'Customer_Satisfaction': np.random.uniform(3.0, 5.0, 10).round(1),
    # Simulate some approximate coordinates for the cities
    'Latitude': [47.6062, 47.6062, 45.5051, 30.2672, 32.7767, 29.7604, 40.7128, 42.3601, 37.7749, 34.0522],
    'Longitude': [-122.3321, -122.3321, -122.6750, -97.7431, -96.7970, -95.3698, -74.0060, -71.0589, -122.4194, -118.2437]
}

df_complex = pd.DataFrame(data)

print("Simulated Complex Dashboard Dataset:")
print(df_complex)

# Note: This is a very small simulated dataset for demonstration.
# A real-world dataset would be much larger and require more extensive
# data cleaning and feature engineering.

# Potential Feature Engineering for Predictive Analysis:
# - Create interaction terms between features.
# - One-hot encode categorical features if using models that require numerical input.
# - Scale numerical features.

# For this preparatory step, we will keep the data simple and directly use
# the existing numerical and categorical columns.

# Data formatting for visualizations:
# - Hierarchical data is already in a suitable format for sunburst/treemap (multiple columns).
# - Numerical data is ready for scatter plots and other charts.
# - Geographical data (Latitude, Longitude) is ready for map visualizations.