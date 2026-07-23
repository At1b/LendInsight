from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    Image,
    KeepTogether
)

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import inch
from reportlab.lib import colors

from datetime import datetime
import os


styles = getSampleStyleSheet()

TITLE_STYLE = ParagraphStyle(
    "TitleStyle",
    parent=styles["Title"],
    alignment=TA_CENTER,
    fontName="Helvetica-Bold",
    fontSize=22,
    textColor=colors.HexColor("#0B5394"),
    spaceAfter=6,
    spaceBefore=0,
)

HEADING_STYLE = ParagraphStyle(
    "HeadingStyle",
    parent=styles["Heading1"],
    textColor=colors.HexColor("#0B5394"),
    fontName="Helvetica-Bold",
    fontSize=13,
    spaceBefore=10,
    spaceAfter=6,
)

SUB_STYLE = ParagraphStyle(
    "SubHeading",
    parent=styles["Heading2"],
    textColor=colors.HexColor("#1F4E79"),
    fontSize=12,
    spaceBefore=0,
    spaceAfter=4,
)

BODY_STYLE = ParagraphStyle(
    "BodyStyle",
    parent=styles["BodyText"],
    fontSize=9,
    leading=14,
    spaceAfter=4,
    spaceBefore=0,
)


def add_header_footer(canvas, doc):

    canvas.saveState()

    canvas.setFont("Helvetica-Bold", 9)
    canvas.setFillColor(colors.HexColor("#0B5394"))
    canvas.drawString(40, 810, "LendInsight Analytics Platform")

    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawRightString(560, 20, f"Page {doc.page}")

    canvas.restoreState()

    
def create_kpi_table(total_customers, average_income, high_risk, states):

    data = [
        ["KPI", "Value"],
        ["Total Customers", f"{total_customers:,}"],
        ["Average Income", f"₹{average_income:,.2f}"],
        ["High Risk Customers", f"{high_risk:,}"],
        ["States Covered", str(states)]
    ]

    table = Table(data, colWidths=[250, 180])

    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0),(-1,0), colors.HexColor("#0B5394")),
        ("TEXTCOLOR",(0,0),(-1,0), colors.white),
        ("FONTNAME",(0,0),(-1,0), "Helvetica-Bold"),
        ("FONTSIZE",(0,0),(-1,-1), 9),
        ("ALIGN",(0,0),(-1,-1), "CENTER"),
        ("GRID",(0,0),(-1,-1), 0.5, colors.grey),
        ("BACKGROUND",(0,1),(-1,-1), colors.beige),
        ("BOTTOMPADDING",(0,0),(-1,0), 8),
        ("TOPPADDING",(0,0),(-1,-1), 5),
        ("BOTTOMPADDING",(0,1),(-1,-1), 5),
    ]))

    return table


def create_model_table(metrics):

    data = [
        ["Metric", "Score"],
        ["Accuracy", f"{metrics['Accuracy']:.2%}"],
        ["Precision", f"{metrics['Precision']:.2%}"],
        ["Recall", f"{metrics['Recall']:.2%}"],
        ["F1 Score", f"{metrics['F1 Score']:.2%}"]
    ]

    table = Table(data, colWidths=[250,180])

    table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0), colors.HexColor("#2E8B57")),
        ("TEXTCOLOR",(0,0),(-1,0), colors.white),
        ("FONTNAME",(0,0),(-1,0), "Helvetica-Bold"),
        ("FONTSIZE",(0,0),(-1,-1), 9),
        ("ALIGN",(0,0),(-1,-1), "CENTER"),
        ("GRID",(0,0),(-1,-1), 0.5, colors.grey),
        ("BACKGROUND",(0,1),(-1,-1), colors.whitesmoke),
        ("TOPPADDING",(0,0),(-1,-1), 5),
        ("BOTTOMPADDING",(0,0),(-1,-1), 5),
    ]))

    return table


def create_feature_table(feature_df):

    data = [["Feature","Importance"]]

    feature_df = feature_df.sort_values("Importance", ascending=False)

    for _, row in feature_df.iterrows():
        data.append([row["Feature"], f"{row['Importance']:.4f}"])

    table = Table(data,colWidths=[250,180])

    table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0), colors.HexColor("#8B0000")),
        ("TEXTCOLOR",(0,0),(-1,0), colors.white),
        ("FONTNAME",(0,0),(-1,0), "Helvetica-Bold"),
        ("FONTSIZE",(0,0),(-1,-1), 9),
        ("GRID",(0,0),(-1,-1), 0.5, colors.grey),
        ("BACKGROUND",(0,1),(-1,-1), colors.beige),
        ("ALIGN",(0,0),(-1,-1), "CENTER"),
        ("TOPPADDING",(0,0),(-1,-1), 5),
        ("BOTTOMPADDING",(0,0),(-1,-1), 5),
    ]))

    return table


def create_states_table(states_df):

    data = [["State", "Customers"]]

    states_df = states_df.head(10)

    for _, row in states_df.iterrows():
        data.append([row["state"], f"{row['customers']:,}"])

    table = Table(data, colWidths=[250,180])

    table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#1565C0")),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
        ("FONTSIZE",(0,0),(-1,-1), 9),
        ("GRID",(0,0),(-1,-1),0.5,colors.grey),
        ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
        ("TOPPADDING",(0,0),(-1,-1), 5),
        ("BOTTOMPADDING",(0,0),(-1,-1), 5),
    ]))

    return table


def create_profession_table(profession_df):

    data = [["Profession", "Customers"]]

    profession_df = profession_df.head(10)

    for _, row in profession_df.iterrows():
        data.append([row["profession"], f"{row['customers']:,}"])

    table = Table(data,colWidths=[250,180])

    table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#6A1B9A")),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
        ("FONTSIZE",(0,0),(-1,-1), 9),
        ("GRID",(0,0),(-1,-1),0.5,colors.grey),
        ("BACKGROUND",(0,1),(-1,-1),colors.beige),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
        ("TOPPADDING",(0,0),(-1,-1), 5),
        ("BOTTOMPADDING",(0,0),(-1,-1), 5),
    ]))

    return table


def generate_report(
        filename,
        total_customers,
        average_income,
        high_risk,
        states,
        metrics,
        feature_df,
        states_df,
        profession_df
):

    doc = SimpleDocTemplate(
        filename,
        rightMargin=40,
        leftMargin=40,
        topMargin=50,
        bottomMargin=40
    )

    elements = []

    # ── Cover Page ──
    elements.append(Spacer(1, 2 * inch))
    elements.append(Paragraph("LendInsight", TITLE_STYLE))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph("Analytics & Business Intelligence Report", SUB_STYLE))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(
        f"Generated on: {datetime.now().strftime('%d %B %Y, %I:%M %p')}",
        BODY_STYLE
    ))
    elements.append(PageBreak())

    # ── All content sections use KeepTogether to prevent orphaned headings ──

    # Executive Summary
    elements.append(KeepTogether([
        Paragraph("Executive Summary", HEADING_STYLE),
        Paragraph(
            "LendInsight is an Analytics & Business Intelligence platform "
            "developed to analyze customer loan data, identify high-risk "
            "applicants using Machine Learning, segment customers using "
            "K-Means clustering, and generate actionable insights for "
            "financial institutions. This report summarizes customer demographics, "
            "predictive analytics, and business recommendations that support "
            "data-driven lending decisions.",
            BODY_STYLE
        ),
        Spacer(1, 6),
    ]))

    # KPI Dashboard
    elements.append(KeepTogether([
        Paragraph("Key Performance Indicators", HEADING_STYLE),
        create_kpi_table(total_customers, average_income, high_risk, states),
        Spacer(1, 8),
    ]))

    # Model Performance
    elements.append(KeepTogether([
        Paragraph("Machine Learning Performance", HEADING_STYLE),
        create_model_table(metrics),
        Spacer(1, 8),
    ]))

    # Feature Importance
    elements.append(KeepTogether([
        Paragraph("Feature Importance", HEADING_STYLE),
        create_feature_table(feature_df),
        Spacer(1, 8),
    ]))

    # State Analysis
    elements.append(KeepTogether([
        Paragraph("Top States", HEADING_STYLE),
        create_states_table(states_df),
        Spacer(1, 8),
    ]))

    # Profession Analysis
    elements.append(KeepTogether([
        Paragraph("Top Professions", HEADING_STYLE),
        create_profession_table(profession_df),
        Spacer(1, 8),
    ]))

    # Segmentation
    elements.append(KeepTogether([
        Paragraph("Customer Segmentation", HEADING_STYLE),
        Paragraph(
            "Customers are segmented into Premium, Regular and Budget groups using "
            "K-Means Clustering based on income, age, experience, current job years, "
            "and current house years. These segments help financial institutions "
            "personalize loan offerings and improve customer relationship management.",
            BODY_STYLE
        ),
        Spacer(1, 4),
    ]))

    # Risk Summary
    elements.append(KeepTogether([
        Paragraph("Risk Analysis", HEADING_STYLE),
        Paragraph(
            "The Random Forest classifier predicts customer loan risk using demographic "
            "and financial attributes. High-risk applicants can be prioritized for "
            "manual review while low-risk customers can benefit from faster loan approval, "
            "improving operational efficiency.",
            BODY_STYLE
        ),
        Spacer(1, 4),
    ]))

    # Recommendations
    rec_items = [Paragraph("Business Recommendations", HEADING_STYLE)]
    for r in [
        "• Prioritize manual verification for customers predicted as High Risk.",
        "• Design personalized loan products using customer segmentation.",
        "• Monitor state-wise customer trends to optimize lending strategies.",
        "• Regularly retrain the Machine Learning model using fresh customer data.",
        "• Use feature importance analysis to improve underwriting policies.",
        "• Build executive dashboards for continuous portfolio monitoring.",
    ]:
        rec_items.append(Paragraph(r, BODY_STYLE))
    rec_items.append(Spacer(1, 6))
    elements.append(KeepTogether(rec_items))

    # Conclusion
    elements.append(KeepTogether([
        Paragraph("Conclusion", HEADING_STYLE),
        Paragraph(
            "LendInsight demonstrates how Business Intelligence, "
            "SQL Analytics and Machine Learning can be integrated "
            "into a single platform for modern financial institutions. "
            "The solution enables customer segmentation, predictive "
            "loan risk assessment, analytical reporting and "
            "executive-level decision support through an "
            "interactive dashboard and automated PDF reports.",
            BODY_STYLE
        ),
    ]))

    doc.build(
        elements,
        onFirstPage=add_header_footer,
        onLaterPages=add_header_footer
    )
