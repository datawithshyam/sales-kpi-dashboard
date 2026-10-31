import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Sales Performance Dashboard", layout="wide", page_icon="📈"
)

st.title("📈 Executive Sales & Revenue Analytics")
st.markdown(
    "Real-time KPI tracker for monthly sales performance and order volume."
)

# Sample business sales data
sales_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
    "Revenue": [18000, 24000, 21000, 32000, 39000, 45000, 52000],
    "Orders": [190, 260, 230, 340, 410, 480, 560],
    "Avg_Order_Value": [94.7, 92.3, 91.3, 94.1, 95.1, 93.7, 92.8],
}
df = pd.DataFrame(sales_data)

# KPI Metrics Row
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${df['Revenue'].sum():,}", "+15.5%")
col2.metric("Total Orders", f"{df['Orders'].sum():,}", "+18.2%")
col3.metric(
    "Avg Order Value", f"${round(df['Avg_Order_Value'].mean(), 2)}", "+1.2%"
)

# Interactive Chart
fig = px.bar(
    df,
    x="Month",
    y="Revenue",
    color="Revenue",
    text_auto=".2s",
    title="Monthly Revenue Trend (USD)",
    color_continuous_scale="Blues",
)
st.plotly_chart(fig, use_container_width=True)
