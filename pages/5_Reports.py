import streamlit as st
from utils.data_loader import load_data
from models.forecasting import train_model
from utils.pdf_generator import generate_report
from utils.sql_queries import (
    get_top_states,
    get_top_professions
)

import pandas as pd
import os

from utils.helpers import (
    inject_custom_css, sidebar_branding, styled_header,
    styled_kpi_card, section_header, section_divider,
    status_badge, BI_BLUE, BI_RED, BI_PURPLE, BI_TEAL,
)

st.set_page_config(page_title="Reports", layout="wide")

inject_custom_css()
sidebar_branding()

styled_header("Reports",
    "Generate a professional analytics report in PDF format.", "📄")

# Load data
df = load_data()

# Load trained model metrics
model, metrics, X, y_test, y_pred, feature_names = train_model()

feature_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": model.feature_importances_
})

states_df = get_top_states()
profession_df = get_top_professions()

# Calculate KPIs
total_customers = len(df)
average_income = df["income"].mean()
high_risk = df["risk_flag"].sum()
states = df["state"].nunique()

section_header("Report Preview", "👁️")

st.markdown("""
<p style="
    font-family: 'Inter', sans-serif; font-size: 0.88rem;
    color: #64748B; margin-bottom: 1rem;
">The following KPIs will be included in your generated report.</p>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    styled_kpi_card("Total Customers", f"{total_customers:,}", "👥", BI_BLUE)
with col2:
    styled_kpi_card("Average Income", f"₹{average_income:,.0f}", "💰", BI_PURPLE)
with col3:
    styled_kpi_card("High Risk Customers", f"{high_risk:,}", "⚠️", BI_RED)
with col4:
    styled_kpi_card("States Covered", f"{states}", "🗺️", BI_TEAL)

section_divider()

section_header("Report Contents", "📑")

st.markdown("""
<div style="
    background: #FFFFFF; border: 1px solid #E2E8F0;
    border-radius: 14px; padding: 1.5rem; margin-bottom: 1.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
        <div style="font-family: 'Inter', sans-serif; font-size: 0.85rem; color: #334155;
            display: flex; align-items: center; gap: 0.5rem;">
            <span style="color: #22C55E; font-weight: 700;">✓</span> Executive Summary</div>
        <div style="font-family: 'Inter', sans-serif; font-size: 0.85rem; color: #334155;
            display: flex; align-items: center; gap: 0.5rem;">
            <span style="color: #22C55E; font-weight: 700;">✓</span> Key Performance Indicators</div>
        <div style="font-family: 'Inter', sans-serif; font-size: 0.85rem; color: #334155;
            display: flex; align-items: center; gap: 0.5rem;">
            <span style="color: #22C55E; font-weight: 700;">✓</span> ML Model Performance</div>
        <div style="font-family: 'Inter', sans-serif; font-size: 0.85rem; color: #334155;
            display: flex; align-items: center; gap: 0.5rem;">
            <span style="color: #22C55E; font-weight: 700;">✓</span> Feature Importance Analysis</div>
        <div style="font-family: 'Inter', sans-serif; font-size: 0.85rem; color: #334155;
            display: flex; align-items: center; gap: 0.5rem;">
            <span style="color: #22C55E; font-weight: 700;">✓</span> State & Profession Analytics</div>
        <div style="font-family: 'Inter', sans-serif; font-size: 0.85rem; color: #334155;
            display: flex; align-items: center; gap: 0.5rem;">
            <span style="color: #22C55E; font-weight: 700;">✓</span> Business Recommendations</div>
    </div>
</div>
""", unsafe_allow_html=True)

section_header("Generate Report", "🖨️")

if st.button("📄 Generate PDF Report"):

    filename = "reports/LendInsight_Report.pdf"

    generate_report(
        filename=filename,
        total_customers=total_customers,
        average_income=average_income,
        high_risk=high_risk,
        states=states,
        metrics=metrics,
        feature_df=feature_df,
        states_df=states_df,
        profession_df=profession_df
    )

    status_badge("Report generated successfully", "success")

    st.markdown("<div style='height: 0.75rem;'></div>", unsafe_allow_html=True)

    with open(filename, "rb") as pdf:
        st.download_button(
            label="⬇ Download Report",
            data=pdf,
            file_name="LendInsight_Report.pdf",
            mime="application/pdf"
        )