import pickle
import streamlit as st
import numpy as np
import pydantic
from pydantic import BaseModel

with open(r"E:\End to End ML projects\1st ML project\model.pkl", 'rb') as f:
    model=pickle.load(f)

class modelvalidation(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History : float
    Property_Area: str

def predictions(details: modelvalidation):
    data=details.dict()
    Gender=data['Gender']
    Married=data['Married']
    Dependents= data['Dependents']
    Education= data['Education']
    Self_Employed= data['Self_Employed']
    ApplicantIncome= data['ApplicantIncome']
    CoapplicantIncome= data['CoapplicantIncome']
    LoanAmount= data['LoanAmount']
    Loan_Amount_Term= data['Loan_Amount_Term']
    Credit_History= data['Credit_History']
    Property_Area= data['Property_Area']
    
    if Gender=='Male':
        Gender=1
    else:
        Gender=0
    
    if Married=='No':
        Married=0
    else:
        Married=1
    
    if Dependents=='0':
        Dependents=0
    elif Dependents=='1':
        Dependents=1
    elif Dependents=='2':
        Dependents=2
    elif Dependents=='3+':
        Dependents=3
    
    if Education=='Graduate':
        Education=0
    else:
        Education=1
    
    if Self_Employed=='No':
        Self_Employed=0
    else:
        Self_Employed=1
    
    if Property_Area=='Rural':
        Property_Area=0
    elif Property_Area=='Semiurban':
        Property_Area=1
    else:
        Property_Area=2



    prediction=model.predict([[Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, Loan_Amount_Term
                              , LoanAmount, Credit_History, Property_Area]])
    
    if prediction==0:
        return "Sorry ! Your loan cannot be sanctioned"
    
    else:
        return "Congrats! You are eligible for loan , our team will get back to you"

def main():
    st.title("Welcome to loan prediction application")
    st.header("Please enter the requested details")

    Gender=st.selectbox("Select gender", ("Male", "Female"))
    Married=st.selectbox("Married", ("Yes", "No"))
    Dependents=st.text_input("No of dependents")
    Education=st.text_input("Enter education level")
    Self_Employed=st.selectbox("Self_employed", ("Yes", "No"))
    ApplicantIncome=st.text_input("Enter income")
    CoapplicantIncome=st.text_input("Co applicant income")
    LoanAmount= st.text_input("Enter expected loan amount")
    Loan_Amount_Term=st.text_input("Enter loan term")
    Credit_History=st.text_input("Enter_credit history")
    Property_Area=st.text_input("Enter property area")

    ###backend

    response=st.button("Submit")

    if response==True:
        #response=predictions()
        data = {"Gender": Gender,
                "Married": Married,
                "Dependents": Dependents,
                "Education": Education,
                "Self_Employed": Self_Employed,
                "ApplicantIncome": float(ApplicantIncome), 
                "CoapplicantIncome": float(CoapplicantIncome),
                "LoanAmount": float(LoanAmount),
                "Loan_Amount_Term": float(Loan_Amount_Term),
                "Credit_History": float(Credit_History),
                "Property_Area": Property_Area}
        details=modelvalidation(**data)
        prediction=predictions(details)
        # prediction=predictions(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome,
        #                      LoanAmount, Loan_Amount_Term, Credit_History, Property_Area )
        

        st.text(prediction)
        


if __name__=='__main__':
    main()
