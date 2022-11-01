import argparse
import os
# import json
# import click
# import mlflow
# from typing import Tuple, Dict

# import logging.config
# from src.settings import get_logging_conf

# from src.data import read_data, split_train_val_data
# from src.features import extract_target, build_transformer
# from src.models import evaluate_model, train_model, predict_model, dump_model
# from src.enities import read_train_pipeline_params, TrainingPipelineParams

# logging.config.dictConfig(get_logging_conf())
# logger = logging.getLogger(__name__)


# def train_pipeline(train_pipeline_params: TrainingPipelineParams) -> Tuple[str, Dict[str, float]]:
#     logger.info(f"start train pipeline with params {train_pipeline_params}")
#     data = read_data(train_pipeline_params.path_to_data)
#     logger.info(f"data.shape is {data.shape}")

#     train_df, val_df = split_train_val_data(
#         data, train_pipeline_params.splitting_params
#     )
#     train_df, train_target = extract_target(train_df, train_pipeline_params.feature_params)
#     val_df, val_target = extract_target(val_df, train_pipeline_params.feature_params)
#     logger.info(f"train_df.shape is {train_df.shape}")
#     logger.info(f"val_df.shape is {val_df.shape}")

#     transformer = build_transformer(train_pipeline_params.feature_params)
#     train_features = transformer.fit_transform(train_df)
#     logger.info(f"train_features.shape is {train_features.shape}")

#     model = train_model(train_features, train_target, train_pipeline_params.train_params)

#     val_features = transformer.transform(val_df)
#     predicts = predict_model(val_features, model)

#     metrics = evaluate_model(predicts, val_target)
#     logger.info(f"metrics is {metrics}")

#     with open(train_pipeline_params.path_to_metrics, "w") as f:
#         json.dump(metrics, f)
#         logger.info(f"metrics saved by {train_pipeline_params.path_to_metrics}")

#     with mlflow.start_run(run_name=f'training model {train_pipeline_params.train_params.model_type}'):
#         mlflow.sklearn.log_model(model, train_pipeline_params.train_params.model_type)
#         for metric, score in metrics.items():
#             mlflow.log_metric(metric, score)
#         logger.info("metrics tracking by mlflow")

#     path_to_model = dump_model(model, train_pipeline_params.path_to_output)
#     logger.info(f"model saved by {train_pipeline_params.path_to_output}")
#     return path_to_model, metrics


# @click.command()
# @click.argument("config_path", default='configs/train_log_reg_with_scaler.yaml',
#                 type=click.Path(exists=True))
# def train_pipeline_command(config_path: str):
#     params = read_train_pipeline_params(config_path)
#     train_pipeline(params)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Training')
    parser.add_argument('config_path', type=str, choices=DATASETS)
    args = parser.parse_args()
    params = read_train_pipeline_params(parser.config_path)
    train_pipeline(params)
    # train_pipeline_command()