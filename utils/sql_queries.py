import os
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
def get_total_customers():
    query = "SELECT COUNT(*) FROM loan_data;"
    return pd.read_sql(query, engine).iloc[0, 0]


@st.cache_data
def get_average_income():
    query = "SELECT ROUND(AVG(income),2) FROM loan_data;"
    return pd.read_sql(query, engine).iloc[0, 0]


@st.cache_data
def get_high_risk_customers():
    query = "SELECT COUNT(*) FROM loan_data WHERE risk_flag=1;"
    return pd.read_sql(query, engine).iloc[0, 0]


@st.cache_data
def get_total_states():
    query = "SELECT COUNT(DISTINCT state) FROM loan_data;"
    return pd.read_sql(query, engine).iloc[0, 0]


@st.cache_data
def get_top_states():
    query = """
    SELECT state, COUNT(*) AS customers
    FROM loan_data
    GROUP BY state
    ORDER BY customers DESC
    LIMIT 10;
    """
    return pd.read_sql(query, engine)


@st.cache_data
def get_top_professions():
    query = """
    SELECT profession, COUNT(*) AS customers
    FROM loan_data
    GROUP BY profession
    ORDER BY customers DESC
    LIMIT 10;
    """
    return pd.read_sql(query, engine)


@st.cache_data
def get_risk_by_state():
    query = """
    SELECT
        state,
        ROUND(100.0 * SUM(risk_flag) / COUNT(*),2) AS risk_percentage
    FROM loan_data
    GROUP BY state
    ORDER BY risk_percentage DESC;
    """
    return pd.read_sql(query, engine)


@st.cache_data
def get_average_income_by_state():
    query = """
    SELECT state,
           ROUND(AVG(income),2) AS average_income
    FROM loan_data
    GROUP BY state
    ORDER BY average_income DESC;
    """
    return pd.read_sql(query, engine)


@st.cache_data
def get_top_income_professions():
    query = """
    SELECT profession,
           ROUND(AVG(income),2) AS average_income
    FROM loan_data
    GROUP BY profession
    ORDER BY average_income DESC
    LIMIT 10;
    """
    return pd.read_sql(query, engine)


@st.cache_data
def get_age_distribution():
    query = """
    SELECT age, COUNT(*) AS customers
    FROM loan_data
    GROUP BY age
    ORDER BY age;
    """
    return pd.read_sql(query, engine)


@st.cache_data
def get_marital_status():
    query = """
    SELECT marital_status, COUNT(*) AS customers
    FROM loan_data
    GROUP BY marital_status;
    """
    return pd.read_sql(query, engine)


@st.cache_data
def get_house_ownership():
    query = """
    SELECT house_ownership, COUNT(*) AS customers
    FROM loan_data
    GROUP BY house_ownership;
    """
    return pd.read_sql(query, engine)


@st.cache_data
def get_car_ownership():
    query = """
    SELECT car_ownership, COUNT(*) AS customers
    FROM loan_data
    GROUP BY car_ownership;
    """
    return pd.read_sql(query, engine)