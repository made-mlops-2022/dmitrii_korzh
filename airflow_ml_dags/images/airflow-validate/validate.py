import os
import pandas as pd
from sklearn.metrics import accuracy_score, roc_auc_score
import click
import pickle
import json



@click.command("validate")
@click.option("--data-dir")
@click.option("--artifacts-dir")
@click.option("--output-dir")
def validate(data_dir: str, artifacts_dir: str, output_dir: str):

    path_data = os.path.join(data_dir, "data_test.csv")
    path_target = os.path.join(data_dir, "target_test.csv")
    test_data = pd.read_csv(path_data)
    test_target = pd.read_csv(path_target)

    path_scaler = os.path.join(artifacts_dir, "scaler.pkl")
    with open(path_scaler, "rb") as file:
        scaler = pickle.load(file)
    scaled_test_data = scaler.transform(test_data)

    path_model = os.path.join(artifacts_dir, "model.pkl")
    with open(path_model, "rb") as file:
        model = pickle.load(file)

    y_pred = model.predict(scaled_test_data)
    y_proba = model.predict_proba(scaled_test_data)[:, 1]
    accuracy = accuracy_score(test_target, y_pred)
    auc = roc_auc_score(y_pred, y_proba)
    metrics = { "accuracy": accuracy, "auc": auc}

    with open(output_dir + "/metrics.pkl", "w") as file:
        json.dump(metrics, file)
    
    with open(output_dir + "/metrics.txt", "w") as file:
        print("Validation metrics:", file=file)
        print(f"Accuracy is {round(accuracy, 3)};", file=file)
        print(f"AUC is {round(auc, 3)};", file=file)


if __name__ == "__main__":
    validate()

