import streamlit as st

st.title("Streamlit columns example")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Sales")
    st.metric("This month", "R12000")

with col2:
    st.header("Growth")
    st.metric("This month", "8%", "+2%")

with col3:
    st.header("Users")
    st.metric("New signups", "320")
    