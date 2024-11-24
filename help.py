import mlflow
print(mlflow.get_tracking_uri())

#mlflow.set_tracking_uri('http://localhost:5000')
#id=mlflow.create_experiment("Loan_prediction")
mlflow.set_experiment("Loan prediction")
id=mlflow.get_experiment_by_name("Loan prediction").experiment_id


with mlflow.start_run(id):
    pass

mlflow.end_run()