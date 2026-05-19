# ==========================================
# MEDICAL STORE SALES DASHBOARD
# ==========================================

# Save this file as: app.py

# Run using:
# streamlit run app.py

# ==========================================
# IMPORT LIBRARIES
# ==========================================

import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Medical Store Dashboard",
    page_icon="💊",
    layout="wide"
)

# ==========================================
# TITLE
# ==========================================

st.title("💊 Medical Store Sales Dashboard")
st.markdown("Analyze medicine sales, revenue, inventory and performance.")

# ==========================================
# SAMPLE DATA
# ==========================================

data = {
    "Medicine": [
        "Paracetamol", "Dolo 650", "Vitamin C",
        "Amoxicillin", "Cough Syrup",
        "Pantoprazole", "Azithromycin",
        "Calcium Tablet", "Insulin", "Ibuprofen"
    ],

    "Category": [
        "Tablet", "Tablet", "Supplement",
        "Capsule", "Syrup",
        "Tablet", "Capsule",
        "Supplement", "Injection", "Tablet"
    ],

    "Sales": [
        18500, 14200, 12800,
        11600, 9500,
        8900, 7800,
        6500, 5400, 4900
    ],

    "Profit": [
        7000, 5200, 4800,
        4300, 3500,
        3100, 2800,
        2400, 2100, 1800
    ]
}

df = pd.DataFrame(data)

# ==========================================
# KPI CALCULATIONS
# ==========================================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
top_product = df.loc[df["Sales"].idxmax(), "Medicine"]

# ==========================================
# KPI CARDS
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="💰 Total Sales",
        value=f"₹{total_sales:,}"
    )

with col2:
    st.metric(
        label="📈 Total Profit",
        value=f"₹{total_profit:,}"
    )

with col3:
    st.metric(
        label="🏆 Top Selling Medicine",
        value=top_product
    )

st.markdown("---")

# ==========================================
# BAR CHART
# ==========================================

st.subheader("📊 Top Selling Medicines")

fig1 = px.bar(
    df,
    x="Medicine",
    y="Sales",
    color="Category",
    text="Sales",
    title="Medicine Sales Analysis"
)

fig1.update_layout(
    xaxis_title="Medicine",
    yaxis_title="Sales Amount"
)

st.plotly_chart(fig1, use_container_width=True)

# ==========================================
# PIE CHART
# ==========================================

col4, col5 = st.columns(2)

with col4:

    st.subheader("💹 Profit Distribution")

    fig2 = px.pie(
        df,
        names="Medicine",
        values="Profit",
        hole=0.4
    )

    st.plotly_chart(fig2, use_container_width=True)

# ==========================================
# CATEGORY SALES
# ==========================================

with col5:

    st.subheader("📦 Category Wise Sales")

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig3 = px.line(
        category_sales,
        x="Category",
        y="Sales",
        markers=True
    )

    st.plotly_chart(fig3, use_container_width=True)

# ==========================================
# DATA TABLE
# ==========================================

st.subheader("📋 Medicine Sales Data")

st.dataframe(df, use_container_width=True)

# ==========================================
# LOW STOCK ALERT
# ==========================================

st.subheader("⚠️ Low Stock Medicines")

low_stock = pd.DataFrame({
    "Medicine": ["Insulin", "Vitamin C", "Cough Syrup"],
    "Stock Left": [15, 20, 10]
})

st.table(low_stock)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")
st.success("✅ Dashboard Developed using Python & Streamlit")