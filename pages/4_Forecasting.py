import streamlit as st
import plotly.express as px
from sklearn.metrics import confusion_matrix
from models.forecasting import train_model
import pandas as pd
import time
from utils.helpers import (
    inject_custom_css, sidebar_branding, styled_header,
    styled_kpi_card, section_header, section_divider,
    apply_chart_style, create_lollipop_chart, CHART_COLORS,
    BI_BLUE, BI_GREEN, BI_RED, BI_TEAL, BI_PURPLE,
)

starts = time.time()

st.set_page_config(page_title="Risk Prediction", layout="wide")

inject_custom_css()
sidebar_branding()

styled_header("Loan Risk Prediction",
    "Random Forest model trained on historical customer data.", "📈")

t1 = time.time()

# Load saved model
model, metrics, X, y_test, y_pred, feature_names = train_model()

st.markdown(f"""
<div style="
    display: inline-flex; align-items: center; gap: 0.5rem;
    background: #22C55E10; border: 1px solid #22C55E25;
    border-radius: 8px; padding: 0.5rem 1rem; margin-bottom: 1rem;
">
    <span style="
        display: inline-block; width: 8px; height: 8px;
        border-radius: 50%; background: #22C55E;
    "></span>
    <span style="
        font-family: 'Inter', sans-serif; font-size: 0.85rem;
        color: #166534; font-weight: 500;
    ">Model loaded in {time.time() - t1:.2f} seconds</span>
</div>
""", unsafe_allow_html=True)

section_header("Model Performance", "🎯")

col1, col2, col3, col4 = st.columns(4)
with col1:
    styled_kpi_card("Accuracy", f"{metrics['Accuracy']:.2%}", "🎯", BI_BLUE)
with col2:
    styled_kpi_card("Precision", f"{metrics['Precision']:.2%}", "🔬", BI_PURPLE)
with col3:
    styled_kpi_card("Recall", f"{metrics['Recall']:.2%}", "📡", BI_GREEN)
with col4:
    styled_kpi_card("F1 Score", f"{metrics['F1 Score']:.2%}", "⚡", "#F59E0B")

section_divider()

section_header("Confusion Matrix", "🔢")

cm = confusion_matrix(y_test, y_pred)

fig = px.imshow(
    cm, text_auto=True,
    labels={"x": "Predicted", "y": "Actual", "color": "Count"},
    x=["Low Risk", "High Risk"],
    y=["Low Risk", "High Risk"],
    color_continuous_scale=[
        [0, "#EFF6FF"],
        [0.3, "#93C5FD"],
        [0.6, "#3B82F6"],
        [1, "#1E40AF"],
    ],
)
apply_chart_style(fig)
fig.update_layout(
    coloraxis_colorbar=dict(
        tickfont=dict(color="#64748B"),
        title_font=dict(color="#64748B"),
    ),
    xaxis=dict(side="bottom"),
)
fig.update_traces(
    textfont=dict(size=22, color="#1E293B", family="Inter, sans-serif"),
    hovertemplate="Actual: %{y}<br>Predicted: %{x}<br>Count: %{z:,}<extra></extra>",
)
st.plotly_chart(fig, use_container_width=True)

section_divider()

section_header("Feature Importance", "📊")

importance_df = (
    pd.DataFrame({
        "Feature": feature_names,
        "Importance": model.feature_importances_
    })
    .sort_values("Importance", ascending=False)
)

fig = create_lollipop_chart(
    importance_df, x_col="Importance", y_col="Feature",
    title="Most Important Features for Risk Prediction",
    color=BI_BLUE,
)
apply_chart_style(fig)
st.plotly_chart(fig, use_container_width=True)

section_divider()

section_header("Predict Customer Risk", "🔮")

st.markdown("""
<p style="
    font-family: 'Inter', sans-serif; font-size: 0.9rem;
    color: #64748B; margin-bottom: 1rem;
">Enter customer details to predict loan risk.</p>
""", unsafe_allow_html=True)

col_left, col_right = st.columns(2)

with col_left:
    income = st.number_input("Income", min_value=0, value=500000)
    age = st.number_input("Age", min_value=18, max_value=100, value=35)
    experience = st.number_input("Experience (Years)", min_value=0, max_value=50, value=10)

with col_right:
    job_years = st.number_input("Current Job Years", min_value=0, max_value=50, value=5)
    house_years = st.number_input("Current House Years", min_value=0, max_value=50, value=8)

st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)

if st.button("🔍 Predict Risk"):

    prediction = model.predict([[
        income, age, experience, job_years, house_years
    ]])[0]

    if prediction == 1:
        st.markdown("""
        <div style="
            background: #FEF2F2; border: 1px solid #FECACA;
            border-left: 4px solid #EF4444;
            border-radius: 12px; padding: 1.5rem; margin: 1rem 0;
            display: flex; align-items: center; gap: 1rem;
        ">
            <span style="font-size: 2rem;">🔴</span>
            <div>
                <div style="
                    font-family: 'Inter', sans-serif; font-size: 1.2rem;
                    font-weight: 700; color: #DC2626;
                ">High Risk Customer</div>
                <div style="
                    font-family: 'Inter', sans-serif; font-size: 0.85rem;
                    color: #64748B; margin-top: 0.2rem;
                ">This applicant is flagged for elevated risk. Manual review recommended.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="
            background: #F0FDF4; border: 1px solid #BBF7D0;
            border-left: 4px solid #22C55E;
            border-radius: 12px; padding: 1.5rem; margin: 1rem 0;
            display: flex; align-items: center; gap: 1rem;
        ">
            <span style="font-size: 2rem;">🟢</span>
            <div>
                <div style="
                    font-family: 'Inter', sans-serif; font-size: 1.2rem;
                    font-weight: 700; color: #16A34A;
                ">Low Risk Customer</div>
                <div style="
                    font-family: 'Inter', sans-serif; font-size: 0.85rem;
                    color: #64748B; margin-top: 0.2rem;
                ">This applicant meets standard risk thresholds. Eligible for streamlined processing.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown(f"""
<div style="
    text-align: right; padding: 1rem 0; margin-top: 2rem;
    border-top: 1px solid #E2E8F0;
">
    <span style="
        font-family: 'Inter', sans-serif; font-size: 0.75rem;
        color: #94A3B8;
    ">Page generated in {time.time() - starts:.2f} seconds</span>
</div>
""", unsafe_allow_html=True)