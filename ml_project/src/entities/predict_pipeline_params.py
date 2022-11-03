from typing import Optional

from dataclasses import dataclass
from marshmallow_dataclass import class_schema
import yaml

from .feature_params import FeatureParams
from .download_params import DownloadParams
from .split_params import SplittingParams
from .feature_params import FeatureParams
from .train_params import TrainingParams

@dataclass()
class PredictPipelineParams:
    path_to_data: str
    path_to_output: str
    path_to_model: str
    feature_params: FeatureParams
    splitting_params: SplittingParams
    feature_params: FeatureParams
    train_params: TrainingParams
    downloading_params: Optional[DownloadParams] = None
    use_mlflow: bool = False
    mlflow_uri: str = "http://18.156.5.226/"
    mlflow_experiment: str = "inference_demo"


PredictPipelineParamsSchema = class_schema(PredictPipelineParams)


def read_predict_pipeline_params(config_path: str) -> PredictPipelineParams:
    with open(config_path, "r") as config:
        schema = PredictPipelineParamsSchema()
        return schema.load(yaml.safe_load(config))




from dataclasses import dataclass

from .download_params import DownloadParams
from .split_params import SplittingParams
from .feature_params import FeatureParams
from .train_params import TrainingParams
from marshmallow_dataclass import class_schema
import yaml


@dataclass()
class TrainingPipelineParams():
    input_data_path: str
    output_model_path: str
    metric_path: str
    splitting_params: SplittingParams
    feature_params: FeatureParams
    train_params: TrainingParams
    downloading_params: Optional[DownloadParams] = None
    use_mlflow: bool = False
    mlflow_uri: str = "http://18.156.5.226/"
    mlflow_experiment: str = "inference_demo"


TrainingPipelineParamsSchema = class_schema(TrainingPipelineParams)


def read_training_pipeline_params(path: str) -> TrainingPipelineParams:
    with open(path, "r") as input_stream:
        schema = TrainingPipelineParamsSchema()
        return schema.load(yaml.safe_load(input_stream))