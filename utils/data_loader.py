""" import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = (
    f"postgresql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)

@st.cache_data
def load_data():
    print("Loading data from the database...")
    query = "SELECT * FROM loan_data;"
    return pd.read_sql(query, engine) """
    
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("data/raw/loan_data.csv")

    df.rename(columns={
        "Id": "id",
        "Income": "income",
        "Age": "age",
        "Experience": "experience",
        "Married/Single": "marital_status",
        "House_Ownership": "house_ownership",
        "Car_Ownership": "car_ownership",
        "Profession": "profession",
        "CITY": "city",
        "STATE": "state",
        "CURRENT_JOB_YRS": "current_job_yrs",
        "CURRENT_HOUSE_YRS": "current_house_yrs",
        "Risk_Flag": "risk_flag"
    }, inplace=True)

    return df