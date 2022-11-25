from fastapi.testclient import TestClient
# from starlette.testclient import TestClient
from main import app
from src.features import COL_ORDER as COLUMNS
from src.utils.utils import load_config
import numpy as np
import requests
import json
import pytest
CULUMNS = [
        "age", "sex", "cp", "trestbps", "chol", "fbs",
        "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"
        ]

client = TestClient(app)


def test_main_part():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()['message'] == "Hello"
    print("Success")

def test_health():
    response = client.get("/health")
    assert 200 == response.status_code

    
def test_predict():
    with client:
        data = [50, 0, 0, 100, 50, 0, 0, 90, 0, 0, 0, 0, 0]
        config = load_config()
        # url = f"http://{config['host']}:{config['port']}/predict/"
        # response = requests.post(url, json={"data": [data], "feature_names": COLUMNS})
        req = {'data': [data], 'feature_names': COLUMNS}
        response = client.post("/predict/", json={"data": [data], "feature_names": COLUMNS})
        assert 200 == response.status_code
        assert response.json()[0]['disease'] == 0

def test_incorrect():
    config = load_config()
    with client:
        url = f"http://{config['host']}:{config['port']}/predict/"
        response = client.post(url, json={"blabla": 0, "dada": "hello"})
        assert response.status_code == 422
