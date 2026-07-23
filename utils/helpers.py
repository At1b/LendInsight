import streamlit as st
import plotly.graph_objects as go


# ─────────────────────────────────────────────
# COLOR PALETTE
# ─────────────────────────────────────────────
COLORS = {
    "bg_page": "#F8FAFC",
    "bg_card": "#FFFFFF",
    "bg_sidebar": "#1E293B",
    "border": "#E2E8F0",
    "border_hover": "#CBD5E1",
    "blue": "#2563EB",
    "purple": "#7C3AED",
    "green": "#22C55E",
    "orange": "#F59E0B",
    "red": "#EF4444",
    "teal": "#0EA5E9",
    "text_dark": "#0F172A",
    "text_primary": "#1E293B",
    "text_secondary": "#64748B",
    "text_muted": "#94A3B8",
}

CHART_COLORS = [
    "#2563EB", "#7C3AED", "#22C55E", "#F59E0B",
    "#EF4444", "#0EA5E9", "#EC4899", "#14B8A6",
    "#F97316", "#6366F1",
]

# ─────────────────────────────────────────────
# SEMANTIC BI COLOR STRATEGY
# ─────────────────────────────────────────────
BI_BLUE = "#2563EB"
BI_GREEN = "#22C55E"
BI_RED = "#EF4444"
BI_ORANGE = "#F59E0B"
BI_PURPLE = "#7C3AED"
BI_GREY = "#94A3B8"
BI_TEAL = "#0EA5E9"


# ─────────────────────────────────────────────
# LOLLIPOP CHART BUILDER
# ─────────────────────────────────────────────
def create_lollipop_chart(df, x_col, y_col, title="", color="#2563EB"):
    """Create a lollipop chart for ranked feature comparison."""
    fig = go.Figure()

    for i, row in df.iterrows():
        fig.add_shape(
            type="line",
            x0=0, x1=row[x_col],
            y0=row[y_col], y1=row[y_col],
            line=dict(color=color, width=2.5),
        )

    fig.add_trace(go.Scatter(
        x=df[x_col],
        y=df[y_col],
        mode="markers+text",
        marker=dict(color=color, size=14, line=dict(color="#FFFFFF", width=2)),
        text=df[x_col].apply(lambda v: f"{v:.4f}"),
        textposition="middle right",
        textfont=dict(color="#64748B", size=11, family="Inter, sans-serif"),
        hovertemplate="%{y}: %{x:.4f}<extra></extra>",
    ))

    fig.update_layout(
        title=title,
        showlegend=False,
        xaxis_title=x_col,
        yaxis_title="",
        yaxis=dict(autorange="reversed"),
    )

    return fig


# ─────────────────────────────────────────────
# PLOTLY TEMPLATE
# ─────────────────────────────────────────────
def get_plotly_layout():
    """Return a clean, light-theme Plotly layout."""
    return dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", color="#1E293B", size=12),
        title_font=dict(size=15, color="#0F172A", family="Inter, sans-serif", weight=600),
        xaxis=dict(
            gridcolor="#F1F5F9",
            zerolinecolor="#E2E8F0",
            tickfont=dict(color="#64748B", size=11),
            title_font=dict(color="#64748B", size=12),
            linecolor="#E2E8F0",
        ),
        yaxis=dict(
            gridcolor="#F1F5F9",
            zerolinecolor="#E2E8F0",
            tickfont=dict(color="#64748B", size=11),
            title_font=dict(color="#64748B", size=12),
            linecolor="#E2E8F0",
        ),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color="#64748B", size=11),
            borderwidth=0,
        ),
        margin=dict(l=40, r=20, t=50, b=40),
        hoverlabel=dict(
            bgcolor="#FFFFFF",
            font_size=12,
            font_color="#1E293B",
            bordercolor="#E2E8F0",
        ),
        colorway=CHART_COLORS,
    )


def apply_chart_style(fig):
    """Apply the clean light Plotly layout to a figure."""
    fig.update_layout(**get_plotly_layout())
    return fig


# ─────────────────────────────────────────────
# STYLED PAGE HEADER
# ─────────────────────────────────────────────
def styled_header(title, subtitle="", icon=""):
    """Render a premium page header."""
    st.markdown(f"""
    <div style="
        padding: 0.25rem 0 1.5rem 0;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #E2E8F0;
    ">
        <h1 style="
            margin: 0; padding: 0;
            font-family: 'Inter', sans-serif;
            font-size: 1.75rem;
            font-weight: 700;
            color: #0F172A;
            letter-spacing: -0.025em;
        ">{icon}  {title}</h1>
        <p style="
            margin: 0.35rem 0 0 0;
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
            color: #64748B;
            font-weight: 400;
        ">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# STYLED KPI CARD
# ─────────────────────────────────────────────
def styled_kpi_card(label, value, icon="📊", accent_color="#2563EB"):
    """Render a premium white KPI card with colored accent."""
    st.markdown(f"""
    <div style="
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 1.25rem 1.4rem;
        margin-bottom: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.03);
        transition: all 0.25s ease;
        position: relative;
        overflow: hidden;
    ">
        <div style="
            position: absolute; top: 0; left: 0; right: 0; height: 3px;
            background: {accent_color};
            border-radius: 14px 14px 0 0;
        "></div>
        <div style="
            display: flex; align-items: center; gap: 0.5rem;
            margin-bottom: 0.6rem; margin-top: 0.2rem;
        ">
            <span style="
                font-size: 1.15rem;
                display: inline-flex; align-items: center; justify-content: center;
                width: 32px; height: 32px;
                background: {accent_color}12;
                border-radius: 8px;
            ">{icon}</span>
            <span style="
                font-family: 'Inter', sans-serif;
                font-size: 0.72rem;
                font-weight: 600;
                color: #64748B;
                text-transform: uppercase;
                letter-spacing: 0.08em;
            ">{label}</span>
        </div>
        <div style="
            font-family: 'Inter', sans-serif;
            font-size: 1.65rem;
            font-weight: 700;
            color: #0F172A;
            line-height: 1.2;
        ">{value}</div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# SECTION DIVIDER
# ─────────────────────────────────────────────
def section_divider():
    st.markdown("""
    <div style="height: 1px; background: #E2E8F0; margin: 2rem 0;"></div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# SECTION HEADER
# ─────────────────────────────────────────────
def section_header(title, icon=""):
    st.markdown(f"""
    <div style="
        display: flex; align-items: center; gap: 0.6rem;
        margin: 1.5rem 0 1rem 0;
    ">
        <span style="font-size: 1.2rem;">{icon}</span>
        <h3 style="
            margin: 0;
            font-family: 'Inter', sans-serif;
            font-size: 1.1rem;
            font-weight: 600;
            color: #0F172A;
        ">{title}</h3>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# INSIGHT CALLOUT CARD
# ─────────────────────────────────────────────
def insight_card(text, icon="💡", color="#2563EB"):
    st.markdown(f"""
    <div style="
        background: {color}08;
        border: 1px solid {color}20;
        border-left: 4px solid {color};
        border-radius: 10px;
        padding: 0.9rem 1.2rem;
        margin: 0.5rem 0;
        display: flex; align-items: center; gap: 0.75rem;
    ">
        <span style="font-size: 1.2rem;">{icon}</span>
        <span style="
            font-family: 'Inter', sans-serif;
            font-size: 0.88rem;
            color: #334155;
            line-height: 1.5;
        ">{text}</span>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# STATUS BADGE
# ─────────────────────────────────────────────
def status_badge(text, status="success"):
    colors_map = {
        "success": ("#22C55E", "#22C55E10", "#166534"),
        "warning": ("#F59E0B", "#F59E0B10", "#92400E"),
        "error": ("#EF4444", "#EF444410", "#991B1B"),
        "info": ("#2563EB", "#2563EB10", "#1E40AF"),
    }
    dot_color, bg, text_color = colors_map.get(status, colors_map["info"])
    st.markdown(f"""
    <div style="
        display: inline-flex; align-items: center; gap: 0.5rem;
        background: {bg}; border: 1px solid {dot_color}25;
        border-radius: 8px; padding: 0.5rem 1rem; margin: 0.5rem 0;
    ">
        <span style="
            display: inline-block; width: 8px; height: 8px;
            border-radius: 50%; background: {dot_color};
        "></span>
        <span style="
            font-family: 'Inter', sans-serif; font-size: 0.85rem;
            color: {text_color}; font-weight: 500;
        ">{text}</span>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# CSS INJECTION
# ─────────────────────────────────────────────
def inject_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }

        /* ── Main Area ── */
        .stApp {
            background: #F8FAFC;
        }

        header[data-testid="stHeader"] {
            background: #FFFFFF;
            border-bottom: 1px solid #E2E8F0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        }

        /* ── Sidebar ── */
        section[data-testid="stSidebar"] {
            background: #1E293B !important;
        }

        section[data-testid="stSidebar"] * {
            color: #CBD5E1 !important;
        }

        section[data-testid="stSidebar"] a {
            color: #E2E8F0 !important;
            font-weight: 500;
            transition: all 0.2s ease;
        }

        section[data-testid="stSidebar"] a:hover {
            color: #FFFFFF !important;
        }

        section[data-testid="stSidebar"] a[aria-selected="true"] {
            color: #FFFFFF !important;
            font-weight: 600;
        }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: #FFFFFF !important;
        }

        /* ── Metric Cards ── */
        div[data-testid="stMetric"] {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 14px;
            padding: 1rem 1.2rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
            transition: all 0.25s ease;
        }

        div[data-testid="stMetric"]:hover {
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            transform: translateY(-1px);
        }

        div[data-testid="stMetric"] label {
            color: #64748B !important;
            font-size: 0.75rem !important;
            font-weight: 600 !important;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }

        div[data-testid="stMetric"] [data-testid="stMetricValue"] {
            color: #0F172A !important;
            font-size: 1.5rem !important;
            font-weight: 700 !important;
        }

        /* ── Dataframes ── */
        .stDataFrame {
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        }

        /* ── Buttons ── */
        .stButton > button {
            background: #2563EB;
            color: #FFFFFF;
            border: none;
            border-radius: 10px;
            padding: 0.6rem 1.5rem;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            font-size: 0.88rem;
            transition: all 0.25s ease;
            box-shadow: 0 1px 3px rgba(37,99,235,0.2);
        }

        .stButton > button:hover {
            background: #1D4ED8;
            box-shadow: 0 4px 14px rgba(37,99,235,0.3);
            transform: translateY(-1px);
            color: #FFFFFF;
        }

        .stButton > button:active {
            transform: translateY(0px);
        }

        /* ── Download Button ── */
        .stDownloadButton > button {
            background: #7C3AED;
            color: #FFFFFF;
            border: none;
            border-radius: 10px;
            padding: 0.6rem 1.5rem;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            font-size: 0.88rem;
            transition: all 0.25s ease;
            box-shadow: 0 1px 3px rgba(124,58,237,0.2);
        }

        .stDownloadButton > button:hover {
            background: #6D28D9;
            box-shadow: 0 4px 14px rgba(124,58,237,0.3);
            transform: translateY(-1px);
            color: #FFFFFF;
        }

        /* ── Number Input ── */
        .stNumberInput input {
            background: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 10px !important;
            color: #1E293B !important;
            font-family: 'Inter', sans-serif !important;
            transition: border-color 0.2s ease;
        }

        .stNumberInput input:focus {
            border-color: #2563EB !important;
            box-shadow: 0 0 0 3px rgba(37,99,235,0.1) !important;
        }

        /* ── Selectbox ── */
        .stSelectbox > div > div {
            background: #FFFFFF;
            border-color: #E2E8F0;
            border-radius: 10px;
        }

        /* ── Alerts ── */
        .stAlert { border-radius: 12px; }

        /* ── Plotly ── */
        .stPlotlyChart {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 14px;
            overflow: hidden;
            padding: 0.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        }

        /* ── Smooth Scrolling ── */
        html { scroll-behavior: smooth; }

        /* ── Hide Branding ── */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* ── HR ── */
        hr {
            border: none; height: 1px;
            background: #E2E8F0; margin: 1.5rem 0;
        }

    </style>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# SIDEBAR BRANDING
# ─────────────────────────────────────────────
def sidebar_branding():
    with st.sidebar:
        st.markdown("""
        <div style="
            padding: 0.75rem 0 1.25rem 0;
            border-bottom: 1px solid #334155;
            margin-bottom: 1rem;
        ">
            <div style="
                display: flex; align-items: center; gap: 0.6rem;
            ">
                <div style="
                    width: 36px; height: 36px;
                    background: linear-gradient(135deg, #2563EB, #7C3AED);
                    border-radius: 10px;
                    display: flex; align-items: center; justify-content: center;
                    font-size: 1.1rem;
                ">📊</div>
                <div>
                    <div style="
                        font-family: 'Inter', sans-serif;
                        font-size: 1.15rem;
                        font-weight: 700;
                        color: #FFFFFF !important;
                        letter-spacing: -0.02em;
                    ">LendInsight</div>
                    <div style="
                        font-family: 'Inter', sans-serif;
                        font-size: 0.62rem;
                        color: #94A3B8 !important;
                        text-transform: uppercase;
                        letter-spacing: 0.12em;
                        font-weight: 500;
                    ">Analytics Platform</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FEATURE CARD
# ─────────────────────────────────────────────
def feature_card(icon, title, description, accent_color="#2563EB"):
    st.markdown(f"""
    <div style="
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 1.5rem;
        height: 100%; min-height: 150px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        transition: all 0.25s ease;
        cursor: default;
        position: relative; overflow: hidden;
    ">
        <div style="
            position: absolute; top: 0; left: 0; right: 0; height: 3px;
            background: {accent_color};
            border-radius: 14px 14px 0 0;
        "></div>
        <div style="
            width: 42px; height: 42px;
            background: {accent_color}10;
            border-radius: 10px;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.4rem;
            margin-bottom: 0.9rem; margin-top: 0.2rem;
        ">{icon}</div>
        <div style="
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            font-weight: 600;
            color: #0F172A;
            margin-bottom: 0.35rem;
        ">{title}</div>
        <div style="
            font-family: 'Inter', sans-serif;
            font-size: 0.8rem;
            color: #64748B;
            line-height: 1.55;
        ">{description}</div>
    </div>
    """, unsafe_allow_html=True)
