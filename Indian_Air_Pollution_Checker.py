# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:59:50 2025

@author: user
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Indian Air Pollution Checker App")
st.text('Alarming Air Quality Crisis: City-wise Breakdown of India"s Polluted Urban Centers')
st.image("Pollution.jpg")
st.video('https://youtu.be/3gbJRF6d604?si=MZ_sjw85NKgvyEA')

df = pd.read_csv("air_pollution_data.csv")
print(df.head())  # Check first few rows
print(df.columns)  # See column names

# Dropdown to select city
cities = df['city'].unique()
selected_city = st.selectbox("Select a city", cities)

# Filter data based on selected city
filtered_data = df[df['city'] == selected_city]

# Line chart for pollution levels over time
fig = px.line(filtered_data, x="date", y="pm2.5", title=f"PM2.5 Levels in {selected_city}")
st.plotly_chart(fig)

# Display raw data if user wants
if st.checkbox("Show raw data"):
    st.write(filtered_data)