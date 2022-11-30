import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
import click

@click.command("preprocess")
@click.option("--input-dir")
@click.option("--output-dir")
def preprocess(input_dir: str, output_dir: str):
    scaler = StandardScaler()
    path = os.path.join(input_dir, "data_train.csv")
    train_data = pd.read_csv(path)
    scaler.fit(train_data)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "scaler.pkl")
    with open(path, "wb") as file:
        pickle.dump(scaler, file)


if __name__ == "__main__":
    preprocess()
