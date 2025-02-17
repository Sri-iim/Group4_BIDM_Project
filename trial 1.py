# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:12:33 2025

@author: Admin
"""

import pandas as pd

# Load the data
data = pd.read_csv('air_pollution_data.csv')

# Display the first few rows
print(data.head())

# Get summary statistics
print(data.describe())

# Check data types and missing values
print(data.info())
