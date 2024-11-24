import streamlit as st

st.title("Loan Prediction application")

st.header("Loan sanction department")

st.subheader("Enter the customer details")

st.text("Hello this an loan application predictor which uses ML algorithms to predict \n loan ")

st.text("Enter your name:  ")
a=st.text_input("name")

st.success(f"Name successfully logged as {a}")
gender=st.radio("Select gender", ('male', 'female'))

if gender=='male':
    st.text("The gender is logged as male")
elif gender=='female':
    st.text("The gender is logged as female")
else:
    st.text("Please enter gender")
