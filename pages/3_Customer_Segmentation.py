import streamlit as st
import plotly.express as px
from models.segmentation import perform_segmentation
from utils.data_loader import load_data

from utils.sql_queries import (
    get_age_distribution,
    get_marital_status,
    get_house_ownership,
    get_car_ownership
)

from utils.helpers import (
    inject_custom_css, sidebar_branding, styled_header,
    styled_kpi_card, section_header, section_divider,
    insight_card, apply_chart_style, CHART_COLORS,
    BI_BLUE, BI_GREEN, BI_RED, BI_PURPLE, BI_TEAL, BI_GREY, BI_ORANGE,
)

st.set_page_config(page_title="Customer Segmentation", layout="wide")

inject_custom_css()
sidebar_branding()

styled_header("Customer Segmentation",
    "Analyze customer demographics before performing segmentation.", "👥")

SEGMENT_COLORS = {
    "Premium Customers": "#F59E0B",
    "Regular Customers": "#2563EB",
    "Budget Customers": "#94A3B8",
}

# ── Age Distribution ──
section_header("Age Distribution", "📊")
raw_df = load_data()
fig = px.histogram(
    raw_df, x="age", nbins=30,
    title="Customer Age Distribution",
    labels={"age": "Age", "count": "Customers"},
)
apply_chart_style(fig)
fig.update_traces(marker_color=BI_BLUE, marker_line_width=0, opacity=0.85)
fig.update_layout(yaxis_title="Customers", bargap=0.05)
st.plotly_chart(fig, use_container_width=True)

section_divider()

# ── Demographics row ──
col1, col2, col3 = st.columns(3)

with col1:
    section_header("Marital Status", "💍")
    marital_df = get_marital_status()
    fig = px.pie(
        marital_df, names="marital_status", values="customers",
        hole=0.5, title="Marital Status",
        color_discrete_sequence=[BI_BLUE, BI_PURPLE],
    )
    apply_chart_style(fig)
    fig.update_traces(
        textinfo="label+percent",
        textfont=dict(color="#1E293B", size=12),
        hovertemplate="%{label}: %{value:,} (%{percent})<extra></extra>",
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    section_header("House Ownership", "🏠")
    house_df = get_house_ownership()
    fig = px.pie(
        house_df, names="house_ownership", values="customers",
        hole=0.5, title="House Ownership",
        color_discrete_sequence=[BI_TEAL, BI_PURPLE, BI_BLUE],
    )
    apply_chart_style(fig)
    fig.update_traces(
        textinfo="label+percent",
        textfont=dict(color="#1E293B", size=12),
        hovertemplate="%{label}: %{value:,} (%{percent})<extra></extra>",
    )
    st.plotly_chart(fig, use_container_width=True)

with col3:
    section_header("Car Ownership", "🚗")
    car_df = get_car_ownership()
    fig = px.pie(
        car_df, names="car_ownership", values="customers",
        hole=0.5, title="Car Ownership",
        color_discrete_sequence=[BI_GREEN, BI_GREY],
    )
    apply_chart_style(fig)
    fig.update_traces(
        textinfo="label+percent",
        textfont=dict(color="#1E293B", size=12),
        hovertemplate="%{label}: %{value:,} (%{percent})<extra></extra>",
    )
    st.plotly_chart(fig, use_container_width=True)

section_divider()

# ── K-Means ──
st.markdown("""
<div style="
    display: flex; align-items: center; gap: 0.6rem;
    margin: 1.5rem 0 1rem 0;
">
    <span style="font-size: 1.3rem;">🤖</span>
    <h2 style="
        margin: 0; font-family: 'Inter', sans-serif;
        font-size: 1.25rem; font-weight: 700; color: #0F172A;
    ">K-Means Customer Segmentation</h2>
</div>
""", unsafe_allow_html=True)

df = perform_segmentation()

cluster_names = {
    0: "Premium Customers",
    1: "Regular Customers",
    2: "Budget Customers"
}

df["Segment"] = df["Cluster"].map(cluster_names)

total_customers = len(df)
premium = len(df[df["Segment"] == "Premium Customers"])
regular = len(df[df["Segment"] == "Regular Customers"])
budget = len(df[df["Segment"] == "Budget Customers"])

col1, col2, col3, col4 = st.columns(4)
with col1:
    styled_kpi_card("Total Customers", f"{total_customers:,}", "👥", BI_BLUE)
with col2:
    styled_kpi_card("Premium", f"{premium:,}", "⭐", "#F59E0B")
with col3:
    styled_kpi_card("Regular", f"{regular:,}", "👤", BI_BLUE)
with col4:
    styled_kpi_card("Budget", f"{budget:,}", "📋", BI_GREY)

section_divider()

left, right = st.columns(2)

with left:
    section_header("Customer Distribution by Segment", "🍩")
    segment_count = df["Segment"].value_counts().reset_index()
    segment_count.columns = ["Segment", "Customers"]

    fig = px.pie(
        segment_count, names="Segment", values="Customers",
        hole=0.5, title="Customer Segments",
        color="Segment", color_discrete_map=SEGMENT_COLORS,
    )
    apply_chart_style(fig)
    fig.update_traces(
        textinfo="label+percent",
        textfont=dict(color="#1E293B", size=13),
        hovertemplate="%{label}: %{value:,} (%{percent})<extra></extra>",
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    section_header("Cluster Summary", "📊")
    summary = (
        df.groupby("Segment")[["income", "age", "experience"]]
        .mean().round(2)
    )
    st.dataframe(summary, use_container_width=True)

    section_header("Business Insights", "💡")
    highest_income = summary["income"].idxmax()
    youngest = summary["age"].idxmin()
    insight_card(f"Highest average income: <strong>{highest_income}</strong>", "💰", "#F59E0B")
    insight_card(f"Youngest customer segment: <strong>{youngest}</strong>", "👶", BI_BLUE)

section_divider()

section_header("Customer Segments Visualization", "🔬")
fig = px.scatter(
    df, x="income", y="age", color="Segment",
    hover_data=["experience", "current_job_yrs"],
    title="Customer Segments based on Income and Age",
    color_discrete_map=SEGMENT_COLORS,
    labels={"income": "Annual Income (₹)", "age": "Age"},
)
apply_chart_style(fig)
fig.update_traces(marker=dict(size=5, opacity=0.7))
st.plotly_chart(fig, use_container_width=True)

section_header("Sample Customer Data", "📋")
st.dataframe(
    df[["income", "age", "experience", "Segment"]].head(20),
    use_container_width=True
)