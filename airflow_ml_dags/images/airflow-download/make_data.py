import os
import click
import pandas as pd
from sklearn.datasets import make_classification


def sample_data(output_dir, n_samples=2000, n_features=5, n_classes=2):
    data, target = make_classification(n_samples=n_samples, n_features=n_features, n_informative=3, n_classes=n_classes)
    pd.DataFrame(data).to_csv(os.path.join(output_dir, "data.csv"), index=False)
    pd.DataFrame(target).to_csv(os.path.join(output_dir, "target.csv"), index=False)


@click.command("download")
@click.argument("output_dir")
def download(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    sample_data(output_dir)

if __name__ == "__main__":
    download()
