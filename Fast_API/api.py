from fastapi import FastAPI
import os
import pickle
import uvicorn
import numpy
import pandas 
import pydantic
from pydantic import BaseModel

# os.chdir(os.curdir+'/Fast_API')

class loan_model(BaseModel):
    Gender: float
    Married: float
    Dependents: float
    Education: float
    Self_Employed: float
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History : float
    Property_Area: float

app=FastAPI()

with open (r"E:\End to End ML projects\1st ML project\model.pkl", 'rb') as f:
    model=pickle.load(f)

#model=pickle.load("E:\End to End ML projects\1st ML project\model.pkl")

@app.get('/')
def root():
    return 'Welcome to the loan predictor app'


@app.post("/predictions")
def predictions(details: loan_model):
    data=details.model_dump()
    gender=data['Gender']
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

    prediction=model.predict([[gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, Loan_Amount_Term
                              , LoanAmount, Credit_History, Property_Area]])
    
    if prediction==0:
        return "Sorry ! Your loan cannot be sanctioned"
    
    else:
        return "Congrats! You are eligible for loan , our team will get back to you"
    

    if __name__=='__main__':
        uvicorn.run(Fast_API.app, host='127.0.0.1', port=8000)