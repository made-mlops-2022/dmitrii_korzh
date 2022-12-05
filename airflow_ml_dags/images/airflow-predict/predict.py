import os
import click
import pandas as pd
import pickle



@click.command("predict")
@click.option("--data-dir")
@click.option("--artifacts-dir")
@click.option("--output-dir")
def predict(data_dir: str, artifacts_dir: str, output_dir: str):
    path = os.path.join(data_dir, "data.csv")
    data = pd.read_csv(path)

    path = os.path.join(artifacts_dir, "scaler.pkl")
    with open(path, "rb") as file:
        scaler = pickle.load(file)

    data = scaler.transform(data)

    path = os.path.join(artifacts_dir, "model.pkl")
    with open(path, "rb") as file:
        model = pickle.load(file)

    probs = model.predict_proba(data)[:, 1]

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "predicts.csv")
    pd.DataFrame(probs).to_csv(path, index=False, header=None)


if __name__ == "__main__":
    predict()
