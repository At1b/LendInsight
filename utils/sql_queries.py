import streamlit as st
from utils.data_loader import load_data


@st.cache_data
def get_total_customers():
    df = load_data()
    return len(df)


@st.cache_data
def get_average_income():
    df = load_data()
    return round(df["income"].mean(), 2)


@st.cache_data
def get_high_risk_customers():
    df = load_data()
    return int(df["risk_flag"].sum())


@st.cache_data
def get_total_states():
    df = load_data()
    return df["state"].nunique()


@st.cache_data
def get_top_states():
    df = load_data()
    return (
        df.groupby("state")
        .size()
        .reset_index(name="customers")
        .sort_values("customers", ascending=False)
        .head(10)
    )


@st.cache_data
def get_top_professions():
    df = load_data()
    return (
        df.groupby("profession")
        .size()
        .reset_index(name="customers")
        .sort_values("customers", ascending=False)
        .head(10)
    )


@st.cache_data
def get_risk_by_state():
    df = load_data()

    result = (
        df.groupby("state")["risk_flag"]
        .mean()
        .mul(100)
        .round(2)
        .reset_index(name="risk_percentage")
        .sort_values("risk_percentage", ascending=False)
    )

    return result


@st.cache_data
def get_average_income_by_state():
    df = load_data()

    return (
        df.groupby("state")["income"]
        .mean()
        .round(2)
        .reset_index(name="average_income")
        .sort_values("average_income", ascending=False)
    )


@st.cache_data
def get_top_income_professions():
    df = load_data()

    return (
        df.groupby("profession")["income"]
        .mean()
        .round(2)
        .reset_index(name="average_income")
        .sort_values("average_income", ascending=False)
        .head(10)
    )


@st.cache_data
def get_age_distribution():
    df = load_data()

    return (
        df.groupby("age")
        .size()
        .reset_index(name="customers")
        .sort_values("age")
    )


@st.cache_data
def get_marital_status():
    df = load_data()

    return (
        df.groupby("marital_status")
        .size()
        .reset_index(name="customers")
    )


@st.cache_data
def get_house_ownership():
    df = load_data()

    return (
        df.groupby("house_ownership")
        .size()
        .reset_index(name="customers")
    )


@st.cache_data
def get_car_ownership():
    df = load_data()

    return (
        df.groupby("car_ownership")
        .size()
        .reset_index(name="customers")
    )