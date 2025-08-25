import streamlit as st

st.title("Sidebar Checkbox Example")

show_data= st.sidebar.checkbox("Show sample data")

if show_data:
    st.write("here is the sample data")
    st.write({
        "Name":[", ice", "Bob", "Charlie"],
        "Score":[80, 90, 78]
    })
else:
    st.write("Use the sidebar to view the data")