import pickle
import streamlit as st
from pydantic import BaseModel, ValidationError

# Load the trained model
with open(r"E:\End to End ML projects\1st ML project\model.pkl", 'rb') as f:
    model = pickle.load(f)

# Define the Pydantic model
class ModelValidation(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str

def predictions(details: ModelValidation):
    data = details.dict()
    Gender = data['Gender']
    Married = data['Married']
    Dependents = data['Dependents']
    Education = data['Education']
    Self_Employed = data['Self_Employed']
    ApplicantIncome = data['ApplicantIncome']
    CoapplicantIncome = data['CoapplicantIncome']
    LoanAmount = data['LoanAmount']
    Loan_Amount_Term = data['Loan_Amount_Term']
    Credit_History = data['Credit_History']
    Property_Area = data['Property_Area']
    
    # Encoding categorical variables
    Gender = 1 if Gender == 'Male' else 0
    Married = 1 if Married == 'Yes' else 0
    Dependents = 3 if Dependents == '3+' else int(Dependents)
    Education = 0 if Education == 'Graduate' else 1
    Self_Employed = 1 if Self_Employed == 'Yes' else 0
    Property_Area = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}[Property_Area]

    prediction = model.predict([[Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, Loan_Amount_Term,
                                 LoanAmount, Credit_History, Property_Area]])
    
    if prediction == 0:
        return "Sorry! Your loan cannot be sanctioned"
    else:
        return "Congrats! You are eligible for a loan. Our team will get back to you."

def main():
    st.title("Welcome to loan prediction application")
    st.header("Please enter the requested details")

    Gender = st.selectbox("Select gender", ("Male", "Female"))
    Married = st.selectbox("Married", ("Yes", "No"))
    Dependents = st.selectbox("No of dependents", ("0", "1", "2", "3+"))
    Education = st.selectbox("Education level", ("Graduate", "Not Graduate"))
    Self_Employed = st.selectbox("Self-employed", ("Yes", "No"))
    ApplicantIncome = st.text_input("Enter income")
    CoapplicantIncome = st.text_input("Co-applicant income")
    LoanAmount = st.text_input("Enter expected loan amount")
    Loan_Amount_Term = st.text_input("Enter loan term")
    Credit_History = st.text_input("Enter credit history")
    Property_Area = st.selectbox("Enter property area", ("Rural", "Semiurban", "Urban"))

    response = st.button("Submit")

    if response:
        try:
            data = {
                "Gender": Gender,
                "Married": Married,
                "Dependents": Dependents,
                "Education": Education,
                "Self_Employed": Self_Employed,
                "ApplicantIncome": float(ApplicantIncome),
                "CoapplicantIncome": float(CoapplicantIncome),
                "LoanAmount": float(LoanAmount),
                "Loan_Amount_Term": float(Loan_Amount_Term),
                "Credit_History": float(Credit_History),
                "Property_Area": Property_Area
            }
            details = ModelValidation(**data)
            prediction = predictions(details)
            st.text(prediction)
        except ValidationError as e:
            st.error(f"Validation error: {e}")

if __name__ == '__main__':
    main()
