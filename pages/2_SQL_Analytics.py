import streamlit as st
import plotly.express as px
from utils import sql_queries as sql
from utils.helpers import (
    inject_custom_css, sidebar_branding, styled_header,
    section_header, section_divider, apply_chart_style,
    CHART_COLORS, BI_BLUE, BI_GREEN, BI_RED, BI_ORANGE, BI_TEAL, BI_PURPLE,
)

st.set_page_config(page_title="SQL Analytics", layout="wide")

inject_custom_css()
sidebar_branding()

styled_header("SQL Analytics Dashboard",
    "Direct PostgreSQL analytics with interactive visualizations", "🗄")

# ── Geographic ──
section_header("Geographic & Demographic Analysis", "🌍")

left, right = st.columns(2)

with left:
    states = sql.get_top_states()
    states_sorted = states.sort_values("customers", ascending=True)

    fig = px.bar(
        states_sorted, x="customers", y="state", orientation="h",
        title="Top 10 States by Customers", text="customers",
    )
    apply_chart_style(fig)
    fig.update_traces(
        marker_color=BI_BLUE, texttemplate="%{text:,}",
        textposition="outside", textfont=dict(color="#64748B", size=11),
    )
    fig.update_layout(yaxis_title="", xaxis_title="Customers")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(states, use_container_width=True)

with right:
    professions = sql.get_top_professions()

    fig = px.treemap(
        professions, path=["profession"], values="customers",
        title="Top 10 Professions by Customers",
        color="customers",
        color_continuous_scale=["#EFF6FF", BI_BLUE],
    )
    apply_chart_style(fig)
    fig.update_traces(
        textinfo="label+value", textfont=dict(size=12),
        hovertemplate="%{label}<br>Customers: %{value:,}<extra></extra>",
    )
    fig.update_layout(coloraxis_showscale=False)
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(professions, use_container_width=True)

section_divider()

# ── Risk ──
section_header("Risk Analysis", "⚠")

risk = sql.get_risk_by_state()
risk_sorted = risk.sort_values("risk_percentage", ascending=True)

fig = px.bar(
    risk_sorted, x="risk_percentage", y="state", orientation="h",
    title="Risk Percentage by State (Sorted Highest → Lowest)",
    text="risk_percentage",
)
apply_chart_style(fig)
fig.update_traces(
    marker_color=BI_ORANGE, texttemplate="%{text:.1f}%",
    textposition="outside", textfont=dict(color="#64748B", size=10),
)
fig.update_layout(
    yaxis_title="", xaxis_title="Risk %",
    height=max(400, len(risk) * 22),
)
st.plotly_chart(fig, use_container_width=True)
st.dataframe(risk, use_container_width=True)

section_divider()

# ── Income ──
section_header("Income Analysis", "💰")

left, right = st.columns(2)

with left:
    income = sql.get_average_income_by_state()
    income_top = income.head(10).sort_values("average_income", ascending=True)

    fig = px.bar(
        income_top, x="average_income", y="state", orientation="h",
        title="Top 10 States by Average Income", text="average_income",
    )
    apply_chart_style(fig)
    fig.update_traces(
        marker_color=BI_TEAL, texttemplate="₹%{text:,.0f}",
        textposition="outside", textfont=dict(color="#64748B", size=10),
    )
    fig.update_layout(yaxis_title="", xaxis_title="Average Income (₹)")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(income, use_container_width=True)

with right:
    profession_income = sql.get_top_income_professions()
    prof_sorted = profession_income.sort_values("average_income", ascending=True)

    fig = px.bar(
        prof_sorted, x="average_income", y="profession", orientation="h",
        title="Highest Income Professions", text="average_income",
    )
    apply_chart_style(fig)
    fig.update_traces(
        marker_color=BI_PURPLE, texttemplate="₹%{text:,.0f}",
        textposition="outside", textfont=dict(color="#64748B", size=10),
    )
    fig.update_layout(yaxis_title="", xaxis_title="Average Income (₹)")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(profession_income, use_container_width=True)