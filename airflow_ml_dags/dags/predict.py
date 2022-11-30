from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime
from docker.types import Mount
from default_args import DEFAULT_ARGS, VOLUME_PATH, RAW_DATA_PATH, PATH_TO_ARTIFACTS, PATH_TO_PREDICTS, TO_MOUNT

with DAG(
        dag_id="predict",
        start_date=datetime(2022, 11, 30),
        schedule_interval="@daily",
        default_args=DEFAULT_ARGS,
) as dag:
    wait_model = FileSensor(
        task_id="wait-model",
        filepath="model_artifacts/{{ ds }}/model.pkl",
        fs_conn_id="MY_CONN",
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke")

    wait_scaler = FileSensor(
        task_id="wait-scaler",
        filepath="model_artifacts/{{ ds }}/scaler.pkl",
        fs_conn_id="MY_CONN",
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke")

    wait_data = FileSensor(
        task_id="wait-for-data",
        filepath="raw/{{ ds }}/data.csv",
        fs_conn_id="MY_CONN",
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke")

    predict = DockerOperator(
        image="airflow-predict",
        command=f"--data-dir={RAW_DATA_PATH} --artifacts-dir={PATH_TO_ARTIFACTS} --output-dir={PATH_TO_PREDICTS}",
        network_mode="bridge",
        task_id="docker-airflow-predict",
        do_xcom_push=False,
        mounts=[Mount(source=VOLUME_PATH, target=TO_MOUNT, type='bind')]
    )

    [wait_model, wait_scaler, wait_data] >> predict
