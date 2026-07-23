import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from utils.data_loader import load_data

@st.cache_resource
def perform_segmentation():

    # Load data
    df = load_data()

    # Select features
    features = [
        "income",
        "age",
        "experience",
        "current_job_yrs",
        "current_house_yrs"
    ]

    data = df[features].copy()

    # Scale features
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Train KMeans
    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    print("Performing segmentation...")
    df["Cluster"] = kmeans.fit_predict(scaled_data)

    return df