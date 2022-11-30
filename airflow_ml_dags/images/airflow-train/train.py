import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
import click
import pickle


@click.command("train")
@click.option("--data-dir")
@click.option("--artifacts-dir")
@click.option("--output-dir")
def train(data_dir: str, artifacts_dir: str, output_dir: str):

    model = LogisticRegression()

    os.makedirs(output_dir, exist_ok=True)
    data = pd.read_csv(os.path.join(data_dir, "data_train.csv"))
    target = pd.read_csv(os.path.join(data_dir, "target_train.csv"))

    path = os.path.join(artifacts_dir, "scaler.pkl")
    with open(path, "rb") as file:
        scaler = pickle.load(file)
    
    data_scaled = scaler.transform(data)

    model.fit(data_scaled, target)
    path = os.path.join(artifacts_dir, "model.pkl")
    with open(path, "wb") as file:
        pickle.dump(model, file)

if __name__ == "__main__":
    train()
