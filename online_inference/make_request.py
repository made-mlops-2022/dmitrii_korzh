import numpy as np
import pandas as pd
import requests
from numpy.random import randint

COL_ORDER = [
        "age", "sex", "cp", "trestbps", "chol", "fbs",
        "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"
        ]
from src.utils.utils import create_logger, load_config

NUM_REQUEST_ORDERS = 2


def generate_data(num_rows) -> pd.DataFrame:

    def generate_random_data():
        data = np.zeros((num_rows, len(COL_ORDER)))
        for i in range(num_rows):
            d = np.array([
                randint(50, 70), randint(0, 1), randint(0, 3), randint(100, 180),
                randint(50, 350), randint(0, 1), randint(0, 2), 
                randint(90, 170), randint(0, 1), randint(0, 9),
                randint(0, 2), randint(0, 3), randint(0, 2)
                ])
            data[i,:] = d
        return data

    data = generate_random_data()
    print(data)
    return pd.DataFrame(data, columns=COL_ORDER)#[COL_ORDER]


if __name__ == "__main__":
    config = load_config()
    logger = create_logger('requests', config['logging'])
    generated_data = generate_data(NUM_REQUEST_ORDERS)
    print(generated_data)
    request_features = COL_ORDER
    
    for i in range(NUM_REQUEST_ORDERS):
        data = [i for i in generated_data.iloc[i].to_list()]
        logger.info(f'requested_data: {data}')
        url = f"http://{config['host']}:{config['port']}/predict/"
        response = requests.post(url, json={"data": [data], "feature_names": request_features})
        logger.info(f'status_code: {response.status_code}')
        logger.info(f'response json: {response.json()}')
