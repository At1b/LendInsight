import streamlit as st
from utils.data_loader import load_data
import utils.sql_queries as sql
import plotly.express as px
from utils.helpers import (
    inject_custom_css, sidebar_branding, styled_header,
    styled_kpi_card, section_header, section_divider,
    apply_chart_style, CHART_COLORS,
    BI_BLUE, BI_GREEN, BI_RED, BI_TEAL, BI_PURPLE,
)

# st.write(sql.__file__)
# st.write(dir(sql))

df = load_data()

st.set_page_config(page_title="Dashboard", layout="wide")

inject_custom_css()
sidebar_branding()

styled_header("Executive Dashboard", "Real-time portfolio KPIs and business analytics", "📊")

total_customers = sql.get_total_customers()
avg_income = sql.get_average_income()
high_risk = sql.get_high_risk_customers()
total_states = sql.get_total_states()

col1, col2, col3, col4 = st.columns(4)
with col1:
    styled_kpi_card("Total Customers", f"{total_customers:,}", "👥", BI_BLUE)
with col2:
    styled_kpi_card("Average Income", f"₹ {avg_income:,.0f}", "💰", BI_PURPLE)
with col3:
    styled_kpi_card("High Risk Customers", f"{high_risk:,}", "⚠️", BI_RED)
with col4:
    styled_kpi_card("States Covered", total_states, "🗺️", BI_TEAL)

section_divider()
section_header("Business Overview", "📈")

left, right = st.columns(2)

with left:
    fig = px.histogram(
        df, x="income", nbins=50,
        title="Income Distribution",
        labels={"income": "Annual Income (₹)", "count": "Customers"},
    )
    apply_chart_style(fig)
    fig.update_traces(marker_color=BI_BLUE, marker_line_width=0, opacity=0.85)
    fig.update_layout(yaxis_title="Customers", bargap=0.05)
    st.plotly_chart(fig, use_container_width=True)

with right:
    risk = df["risk_flag"].value_counts().reset_index()
    risk.columns = ["Risk", "Count"]
    risk["Risk"] = risk["Risk"].map({0: "Low Risk", 1: "High Risk"})

    fig = px.pie(
        risk, values="Count", names="Risk",
        title="Risk Distribution", hole=0.5,
        color="Risk",
        color_discrete_map={"Low Risk": BI_GREEN, "High Risk": BI_RED},
    )
    apply_chart_style(fig)
    fig.update_traces(
        textinfo="label+percent",
        textfont=dict(color="#1E293B", size=13),
        hovertemplate="%{label}: %{value:,} customers (%{percent})<extra></extra>",
        pull=[0, 0.03],
    )
    st.plotly_chart(fig, use_container_width=True)

section_divider()
section_header("Geographic & Demographic Analysis", "🏙️")

left, right = st.columns(2)

with left:
    state = df["state"].value_counts().head(10).reset_index()
    state.columns = ["State", "Customers"]
    state = state.sort_values("Customers", ascending=True)

    fig = px.bar(
        state, x="Customers", y="State", orientation="h",
        title="Top 10 States by Customer Count", text="Customers",
    )
    apply_chart_style(fig)
    fig.update_traces(
        marker_color=BI_BLUE, texttemplate="%{text:,}",
        textposition="outside", textfont=dict(color="#64748B", size=11),
    )
    fig.update_layout(yaxis_title="", xaxis_title="Customers")
    st.plotly_chart(fig, use_container_width=True)

with right:
    profession = df["profession"].value_counts().head(10).reset_index()
    profession.columns = ["Profession", "Customers"]

    fig = px.treemap(
        profession, path=["Profession"], values="Customers",
        title="Top 10 Professions by Customer Count",
        color="Customers",
        color_continuous_scale=["#EFF6FF", BI_BLUE],
    )
    apply_chart_style(fig)
    fig.update_traces(
        textinfo="label+value", textfont=dict(size=12),
        hovertemplate="%{label}<br>Customers: %{value:,}<extra></extra>",
    )
    fig.update_layout(coloraxis_showscale=False)
    st.plotly_chart(fig, use_container_width=True)