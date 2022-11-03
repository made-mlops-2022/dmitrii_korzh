import pickle
from typing import Dict, Union

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, accuracy_score
from sklearn.pipeline import Pipeline

from src.entities.train_params import TrainingParams

SklearnClassificationModels = Union[RandomForestClassifier, LogisticRegression]


def train_model(
    features: pd.DataFrame, target: pd.Series, train_params: TrainingParams
) -> SklearnClassificationModels:
    if train_params.model_type == "RandomForestClassifier":
        model = RandomForestClassifier(
            n_estimators=100, random_state=train_params.random_state
        )
    elif train_params.model_type == "LogisticRegression":
        model = LogisticRegression()
    else:
        raise NotImplementedError()
    model.fit(features, target)
    return model


def load_model(pkl_path, train_params=None):
    with open(pkl_path, 'rb') as file:
        pickle_model = pickle.load(file)
    return pickle_model


def predict_model(
    model: Pipeline, features: pd.DataFrame, use_log_trick: bool = False
) -> np.ndarray:
    predicts = model.predict(features)
    return predicts


def evaluate_model(
    predicts: np.ndarray, target: pd.Series, use_log_trick: bool = False,
    model_name = "RandomForestClassifier"
) -> Dict[str, float]:
    if model_name == "RandomForestClassifier":    
        return {
            "accuracy": accuracy_score(target, predicts)
            # "r2_score": r2_score(target, predicts),
            # "rmse": mean_squared_error(target, predicts, squared=False),
            # "mae": mean_absolute_error(target, predicts),
        }
    else:
        return {
            "accuracy": accuracy_score(target, predicts)
            # will add AUC next time, for this we need return probs

        }



def create_inference_pipeline(
    model: SklearnClassificationModels, transformer: ColumnTransformer
) -> Pipeline:
    return Pipeline([("feature_part", transformer), ("model_part", model)])


def serialize_model(model: object, output: str) -> str:
    with open(output, "wb") as f:
        pickle.dump(model, f)
    return output
