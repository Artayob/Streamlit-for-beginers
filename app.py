import streamlit as st
import pandas as pd
st.title("Sales Dashboard")

st.code("for i in range(5): print(i)", language='python')
# Input widgets

name = st.text_input("Enter your name here:")
age = st.number_input("Enter your age:", min_value=0, max_value=100)
rating = st.slider("Rate the app from 1 to 10:", 1, 10)
city = st.selectbox("Choose your city:", ["New York", "Los angeles", "Cape town"])
show_data= st.checkbox("Show Data")

if show_data:
    st.write("Here is the sample data")
    st.write({"name:":["Alice", "Bob", "Charlie"]})

else:
    st.write("Check the box to see data")

st.header("Monthy sales demo")

st.write(pd.DataFrame({"A": [1,2], "B": [3, 4]}))

# if st.button("Click me"):
#     st.success("Button clicked!")
#     st.balloons()

# st.table(df.head())
st.metric(label="Revenue", value="100000", delta="+5%")

st.sidebar.title("Filters")
options = st.sidebar.selectbox("Select Option", ["North", "South"])
