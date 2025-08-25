import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Sales dashboard", layout="wide")
st.title("Sales Dashboard")
st.markdown("Explore sales, profit, and performance metrics with simple Streamlit charts.")

# Generate Sample Data ----

@st.cache_data
def load_data():
    np.random.seed(42)
    df = pd.DataFrame({
        "Date": pd.date_range(start="2024-01-01", periods=180),
        "Region": np.random.choice(["North", "South", "East", "West"], 180),
        "Sales": np.random.randint(1000, 5000, 180),
        "Profit": np.random.randint(100, 1000, 180)
    })
    return df

df = load_data()

#Sidebar Filters--------------------

st.sidebar.header("Filter Options")
region = st.sidebar.selectbox("Select Region", ["All"] + sorted(df["Region"].unique()))
date_range = st.sidebar.date_input("Select Date Range", (df["Date"].min(), df["Date"].max()))

#Filter data
filtered = df.copy()

if region != "All":
    filtered = filtered[filtered["Region"] == region]

filtered = filtered[
    (filtered["Date"] >= pd.to_datetime(date_range[0])) &
    (filtered["Date"]<= pd.to_datetime(date_range[1]))
]

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${filtered["Sales"].sum():,}")
col2.metric("Average Profit", f"${filtered["Profit"].mean():.2f}")
col3.metric("Total Transactions", len(filtered))

#Charts
st.subheader("Sales Over time")
sales_trend = filtered.groupby("Date")[["Sales", "Profit"]].sum()
st.line_chart(sales_trend)

st.subheader("Sales by Region")
region_summary = filtered.groupby("Region")[["Sales"]].sum().reset_index()
st.bar_chart(region_summary.set_index("Region"))

#Data Preview
with st.expander("View Raw Data"):
    st.dataframe(filtered.reset_index(drop=True))

