import mlflow
print(mlflow.set_experiment("Loan_prediction"))

# id=mlflow.create_experiment("Loan_1")

# with mlflow.start_run(run_name='dummy_run', experiment_id=id):
#     pass


print(mlflow.get_experiment_by_name("Loan_prediction").experiment_id)