from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from loan_model_package.training import model_training


class loan_model(BaseModel):
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

app=FastAPI()

@app.get("/")
def welcome():
    return "Hello welcome to loan predictor app"

@app.post("/prediction")
def predictor(details: loan_model):
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