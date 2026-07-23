import streamlit as st
from utils.helpers import (
    inject_custom_css,
    sidebar_branding,
    feature_card,
    status_badge,
)

st.set_page_config(
    page_title="LendInsight",
    page_icon="📊",
    layout="wide"
)

inject_custom_css()
sidebar_branding()

# ── Hero ──
st.markdown("""
<div style="text-align: center; padding: 2.5rem 1rem 1.5rem 1rem;">
    <div style="
        display: inline-flex; align-items: center; justify-content: center;
        width: 56px; height: 56px;
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        border-radius: 14px; margin-bottom: 1rem;
        font-size: 1.6rem;
    ">📊</div>
    <h1 style="
        font-family: 'Inter', sans-serif;
        font-size: 2.25rem; font-weight: 800;
        color: #0F172A; letter-spacing: -0.03em;
        margin: 0 0 0.4rem 0;
    ">LendInsight</h1>
    <p style="
        font-family: 'Inter', sans-serif;
        font-size: 1.05rem; color: #64748B;
        font-weight: 400; margin: 0;
    ">Business Intelligence & Portfolio Analytics Platform</p>
</div>
""", unsafe_allow_html=True)

status_badge("Connected — Database Online", "success")

st.markdown("""
<div style="height: 1px; background: #E2E8F0; margin: 1.5rem 0 2rem 0;"></div>
<div style="text-align: center; margin-bottom: 1.5rem;">
    <span style="
        font-family: 'Inter', sans-serif; font-size: 0.7rem;
        font-weight: 600; color: #2563EB; text-transform: uppercase;
        letter-spacing: 0.15em;
        background: #2563EB10; padding: 0.3rem 0.8rem; border-radius: 20px;
    ">Platform Capabilities</span>
    <h2 style="
        font-family: 'Inter', sans-serif; font-size: 1.35rem;
        font-weight: 700; color: #0F172A; margin: 0.75rem 0 0 0;
    ">Everything You Need for Lending Analytics</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    feature_card("📈", "Executive KPIs",
        "Real-time key performance indicators for portfolio health, customer base, and risk exposure.",
        "#2563EB")
with col2:
    feature_card("💰", "Income Analytics",
        "Deep-dive into income distributions, state-wise trends, and profession-level benchmarks.",
        "#7C3AED")
with col3:
    feature_card("🏙️", "Geographic Analytics",
        "State and city level customer distribution with interactive visualizations.",
        "#0EA5E9")

st.markdown("<div style='height: 0.75rem;'></div>", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)
with col4:
    feature_card("👔", "Profession Analytics",
        "Customer segmentation by profession with income benchmarking and risk profiling.",
        "#22C55E")
with col5:
    feature_card("⚠️", "Risk Analytics",
        "ML-powered risk prediction with confusion matrices, feature importance, and real-time scoring.",
        "#EF4444")
with col6:
    feature_card("🤖", "Risk Prediction",
        "Random Forest classifier for instant loan risk assessment on new customer profiles.",
        "#F59E0B")

st.markdown("""
<div style="
    text-align: center; padding: 2.5rem 0 1rem 0;
    border-top: 1px solid #E2E8F0; margin-top: 2.5rem;
">
    <span style="
        font-family: 'Inter', sans-serif; font-size: 0.72rem;
        color: #94A3B8;
    ">LendInsight Analytics Platform · Built with Streamlit · Powered by PostgreSQL & Machine Learning</span>
</div>
""", unsafe_allow_html=True)