import unittest
from unittest.mock import patch
import logging
import sys
import src
import os
import numpy as np
import pandas as pd
from numpy.random import randint

from src.data import read_data, split_train_val_data
from src.entities.predict_pipeline_params import (
    PredictPipelineParams,
    read_predict_pipeline_params,
)
from src.entities.train_pipeline_params import (
    TrainingPipelineParams,
    read_training_pipeline_params,
)

from src.features import make_features
from src.features.build_features import extract_target, build_transformer
from src.models import (
    train_model,
    serialize_model,
    predict_model,
    evaluate_model,
)

from src.models.model_fit_predict import create_inference_pipeline
logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

class DoesntExists(Exception):
    logger.info(f"Tests. File with data doesnt exist")


class TestProject(unittest.TestCase):
    
    def test_data_existence(self):
        if os.path.isfile('data/heart_cleveland_upload.csv'):
            pass
        else:
            raise DoesntExists

    def test_predict(self):
        config_path = "config/predict_config_logreg.yaml"
        predict_pipeline_params = read_predict_pipeline_params(config_path)
        _, outputs = src.predict.run_predict_pipeline(predict_pipeline_params)

        self.assertEqual(len(outputs), 297)
        self.assertEqual(isinstance(outputs, np.ndarray), True)
    
    def test_predict_on_random_data(self):
        config_path = "config/predict_config_logreg.yaml"
        predict_pipeline_params = read_predict_pipeline_params(config_path)
        columns = [
            "age", "sex", "cp", "trestbps", "chol", "fbs",
            "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"
            ]
        def generate_data():
            data = [
                randint(50, 70), randint(0, 1), randint(0, 3), randint(100, 180),
                randint(50, 350), randint(0, 1), randint(0, 2), 
                randint(90, 170), randint(0, 1), randint(0, 9),
                randint(0, 2), randint(0, 3), randint(0, 2)
                ]
            return data


        data = generate_data() 
        df = pd.DataFrame([data], columns=columns)
        df.to_csv('data/random_line.csv', index=False)
        predict_pipeline_params.path_to_data = 'data/random_line.csv'
        _, outputs = src.predict.run_predict_pipeline(predict_pipeline_params)

        self.assertEqual(len(outputs), 1)
        self.assertTrue(outputs in [0, 1])
        self.assertTrue(isinstance(outputs, np.ndarray))

    def test_training_procedure(self):
        config_path = "config/train_config_logreg.yaml"
        training_pipeline_params = read_training_pipeline_params(config_path)
        columns = [
            "age", "sex", "cp", "trestbps", "chol", "fbs",
            "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal",
            "condition"
            ]
        def generate_data():
            data = [
                randint(50, 70), randint(0, 1), randint(0, 3), randint(100, 180),
                randint(50, 350), randint(0, 1), randint(0, 2), 
                randint(90, 170), randint(0, 1), randint(0, 9),
                randint(0, 2), randint(0, 3), randint(0, 2),
                randint(0, 1)
                ]
            return data
        data = [generate_data() for i in range(100)]
        df = pd.DataFrame(np.array(data), columns=columns)
        df.to_csv('data/random_train.csv', index=False)
        training_pipeline_params.path_to_data = 'data/random_trine.csv'

        data = read_data(training_pipeline_params.input_data_path)
        train_df, val_df = split_train_val_data(
            data, training_pipeline_params.splitting_params
        )
        b = (len(val_df) / len(data))
        b1 = (b < training_pipeline_params.splitting_params.val_size * 1.1)
        b2 = (b > training_pipeline_params.splitting_params.val_size * 0.9)
        self.assertTrue(b1)
        self.assertTrue(b2)

        val_target = extract_target(val_df, training_pipeline_params.feature_params)

        self.assertEqual(val_target.shape, (60,))
        train_target = extract_target(train_df, training_pipeline_params.feature_params)
        train_df = train_df.drop(training_pipeline_params.feature_params.target_col, 1)
        val_df = val_df.drop(training_pipeline_params.feature_params.target_col, 1)

        transformer = build_transformer(training_pipeline_params.feature_params)
        transformer.fit(train_df)
        train_features = make_features(transformer, train_df)

        model = train_model(
            train_features, train_target, training_pipeline_params.train_params
        )

        inference_pipeline = create_inference_pipeline(model, transformer)
        predicts = predict_model(
            inference_pipeline,
            val_df,
            training_pipeline_params.feature_params.use_log_trick,
        )
        metrics = evaluate_model(
            predicts,
            val_target,
            use_log_trick=False,
            model_name=training_pipeline_params.train_params.model_type
        )
        self.assertGreater(metrics['accuracy'], 0.0)
        self.assertLessEqual(metrics['accuracy'], 1.0)

    def test_transformer(self):
        config_path = "config/train_config_logreg.yaml"
        training_pipeline_params = read_training_pipeline_params(config_path)
        columns = training_pipeline_params.feature_params.numerical_features

        data = read_data(training_pipeline_params.input_data_path)
        full_cols = columns + [training_pipeline_params.feature_params.target_col]
        data = data[full_cols]
        train_df, val_df = split_train_val_data(
            data, training_pipeline_params.splitting_params
        )

        training_pipeline_params.feature_params.categorical_features = []
       
        val_target = extract_target(val_df, training_pipeline_params.feature_params)
        train_target = extract_target(train_df, training_pipeline_params.feature_params)
        train_df = train_df.drop(training_pipeline_params.feature_params.target_col, 1)
        val_df = val_df.drop(training_pipeline_params.feature_params.target_col, 1)

        transformer = build_transformer(training_pipeline_params.feature_params)
        transformer.fit(train_df)
        train_features = make_features(transformer, train_df)

        self.assertGreater(train_features.mean(), -0.3)
        self.assertLess(train_features.mean(), 0.3)

        self.assertGreater(train_features[0].std(), -1.3)
        self.assertLess(train_features[0].std(), 1.3)


if __name__ == '__main__':
    unittest.main()

