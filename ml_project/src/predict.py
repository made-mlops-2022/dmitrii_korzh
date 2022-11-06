import json
import logging
import logging.config
import os
import sys
from pathlib import Path

import click
import pandas as pd
import numpy as np

from src.data import read_data, split_train_val_data
# from src.data.make_dataset import download_data_from_s3
from src.entities.predict_pipeline_params import (
    PredictPipelineParams,
    read_predict_pipeline_params,
)
from src.features import make_features
from src.features.build_features import extract_target, build_transformer
from src.models import (
    train_model,
    serialize_model,
    predict_model,
    evaluate_model,
    load_model
)
# import mlflow
from src.models.model_fit_predict import create_inference_pipeline

from src.logs.return_log_config import return_predict_config
log_config = return_predict_config()
logging.config.dictConfig(log_config)
logger = logging.getLogger()

def predict_pipeline(config_path: str):
    predict_pipeline_params = read_predict_pipeline_params(config_path)
    if predict_pipeline_params.use_mlflow:
        pass

        # mlflow.set_tracking_uri(predict_pipeline_params.mlflow_uri)
        # mlflow.set_experiment(predict_pipeline_params.mlflow_experiment)
        # with mlflow.start_run():
        #     mlflow.log_artifact(config_path)
        #     model_path, metrics = run_train_pipeline(predict_pipeline_params)
        #     mlflow.log_metrics(metrics)
        #     mlflow.log_artifact(model_path)
    else:
        return run_predict_pipeline(predict_pipeline_params)


def run_predict_pipeline(predict_pipeline_params):
    # downloading_params = predict_pipeline_params.downloading_params
    # if downloading_params:
    #     os.makedirs(downloading_params.output_folder, exist_ok=True)
    #     for path in downloading_params.paths:
    #         download_data_from_s3(
    #             downloading_params.s3_bucket,
    #             path,
    #             os.path.join(downloading_params.output_folder, Path(path).name),
    #         )

    logger.info(f"start predict pipeline with params {predict_pipeline_params}")
    data = read_data(predict_pipeline_params.path_to_data)
    logger.info(f"data.shape is {data.shape}")
    train_df, val_df = split_train_val_data(
        data, predict_pipeline_params.splitting_params, True
    )

    # val_target = extract_target(val_df, predict_pipeline_params.feature_params)
    try: # try wether there is a target column
        val_df = val_df.drop(predict_pipeline_params.feature_params.target_col, 1)
    except:
        pass

    logger.info(f"test_df.shape is {val_df.shape}")
    inference_pipeline = load_model(predict_pipeline_params.path_to_model)
    predicts = predict_model(
        inference_pipeline,
        val_df,
        predict_pipeline_params.feature_params.use_log_trick,
    )
    # metrics = evaluate_model(
    #     predicts,
    #     val_target,
    #     use_log_trick=False,
    #     model_name=predict_pipeline_params.train_params.model_type


    # )
    np.save(predict_pipeline_params.path_to_output, np.array(predicts))
    # print(predicts)
    # with open(predict_pipeline_params.path_to_output, "w") as metric_file:
    #     json.dump(list(predicts), metric_file)
    logger.info(f"predicts are {predicts}")
    return inference_pipeline, predicts #, metrics


@click.command(name="predict_pipeline")
@click.argument("config_path")
def predict_pipeline_command(config_path: str):
    predict_pipeline(config_path)


if __name__ == "__main__":
    predict_pipeline_command()
