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
    return pd.read_csv("data/raw/loan_data.csv")    