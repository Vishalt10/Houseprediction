import time
import argparse
import mlflow
import os

### function to pass evaluation metrics
def eval (f1, f2):
    return f1**2+f2**2

## will create a dummy program that takes 2 input variables from users and logs in mlflow

def main (in1, in2):
    mlflow.set_experiment("dummy_test")
    id=mlflow.get_experiment_by_name("dummy_test").experiment_id

    with mlflow.start_run(run_name='dummy_run', experiment_id=id):
        mlflow.log_param("n_estimators", in1)
        mlflow.log_param("criterion", in2)

        mlflow.log_metric("acc", eval(in1, in2))

        os.makedirs("dummy", exist_ok=True)
        with open("dummy/example.txt", 'w') as f:
            f.write(f"The dummy run was successfully logged at {time.asctime()}")

        mlflow.log_artifacts("dummy")

    mlflow.end_run()

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--param1", "-p1", type=int, default=10)
    args.add_argument("--param2", "-p2", type=int, default=20)
    a=args.parse_args()
    main(a.param1, a.param2)