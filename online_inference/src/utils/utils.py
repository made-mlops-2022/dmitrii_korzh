import logging
import os
import pickle
from typing import List, Union
import pandas as pd
import yaml
from fastapi import HTTPException
from pydantic import BaseModel, conlist
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


SklearnClassifiers = Union[LogisticRegression, RandomForestClassifier]
CONFIG_PATH = "src/config.yaml"


def create_logger(name: str, log_config: dict):
    logger = logging.getLogger(name)
    logger.setLevel('DEBUG')
    formatter = logging.Formatter(
        fmt=log_config['format'],
        datefmt=log_config['date_format']
    )
    handler = logging.StreamHandler()
    handler.setLevel(log_config['level'])
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def downoload_checkpoints():
    return 


def load_config():
    path = os.getenv('CONFIG_PATH') or CONFIG_PATH
    with open(path) as fin:
        config = yaml.safe_load(fin)
    return config


def load_object(path: str):
    with open(path, 'rb') as fin:
        obj = pickle.load(fin)
    return obj


class HeartDiseaseModel(BaseModel):
    data: List[conlist(Union[float, int, None], min_items=13, max_items=13)]
    feature_names: List[str]    

class ModelResponse(BaseModel):
    disease: int

def create_inference_pipeline(
    model: SklearnClassifiers, transformer: ColumnTransformer
) -> Pipeline:
    return Pipeline([("feature_part", transformer), ("model_part", model)])

def prediction(data: List, columns: List[str], model: SklearnClassifiers) -> List[ModelResponse]:
    if len(data) == 0:
        raise HTTPException(status_code=400, detail="Empty data")
    data = pd.DataFrame(data, columns=columns)
    predictions = model.predict(data)
    print(predictions)
    return [ModelResponse(disease=predictions)]


