import streamlit as st
import joblib
from utils.download_model import ensure_model
from utils.data_loader import load_data


@st.cache_resource
def train_model():
    ensure_model()
    data = joblib.load("models/random_forest_model.pkl")

    model = data["model"]
    metrics = data["metrics"]
    feature_names = data["feature_names"]
    y_test = data["y_test"]
    y_pred = data["y_pred"]

    df = load_data()

    X = df[
        [
            "income",
            "age",
            "experience",
            "current_job_yrs",
            "current_house_yrs"
        ]
    ]

    return model, metrics, X, y_test, y_pred, feature_names