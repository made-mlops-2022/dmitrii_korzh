from datetime import timedelta


DEFAULT_ARGS = {
    "owner": "admin",
    "email": ["admin@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
    'email_on_failure': True
}

VOLUME_PATH = "/Users/dmitrii/Desktop/MADE/dmitrii_korzh/airflow_ml_dags/data"
TO_MOUNT = "/data"
RAW_DATA_PATH = "/data/raw/{{ ds }}"
PATH_TO_PROCESSED = "/data/processed/{{ ds }}"
PATH_TO_ARTIFACTS = "/data/model_artifacts/{{ ds }}"
PATH_TO_PREDICTS = "/data/predictions/{{ ds }}"

