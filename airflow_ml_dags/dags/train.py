import airflow
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from docker.types import Mount
from default_args import DEFAULT_ARGS, VOLUME_PATH, RAW_DATA_PATH, PATH_TO_PROCESSED, PATH_TO_ARTIFACTS, TO_MOUNT

with DAG(
        dag_id="train",
        start_date=datetime(2022, 11, 30),
        schedule_interval="@daily",
        default_args=DEFAULT_ARGS,
) as dag:

    wait_target = FileSensor(
        task_id="wait-target",
        filepath="raw/{{ ds }}/target.csv",
        fs_conn_id="MY_CONN",
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke")

    wait_data = FileSensor(
        task_id="wait-data",
        filepath="raw/{{ ds }}/data.csv",
        fs_conn_id="MY_CONN",
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke")

    split_data = DockerOperator(
        image="airflow-split",
        command=f"--input-dir={RAW_DATA_PATH} --output-dir={PATH_TO_PROCESSED}",
        network_mode="bridge",
        task_id="docker-airflow-split",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=VOLUME_PATH, target=TO_MOUNT, type='bind')]
    )

    preprocess = DockerOperator(
        image="airflow-preprocess",
        command=f"--input-dir={PATH_TO_PROCESSED} --output-dir={PATH_TO_ARTIFACTS}",
        network_mode="bridge",
        task_id="docker-airflow-scaler",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=VOLUME_PATH, target=TO_MOUNT, type='bind')]
    )

    train = DockerOperator(
        image="airflow-train",
        command=f"--data-dir={PATH_TO_PROCESSED} --artifacts-dir={PATH_TO_ARTIFACTS} --output-dir={PATH_TO_ARTIFACTS}",
        network_mode="bridge",
        task_id="airflow-train-model",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=VOLUME_PATH, target=TO_MOUNT, type='bind')]
    )

    validate = DockerOperator(
        image="airflow-validate",
        command=f"--data-dir={PATH_TO_PROCESSED} --artifacts-dir={PATH_TO_ARTIFACTS} --output-dir={PATH_TO_ARTIFACTS}",
        network_mode="bridge",
        task_id="docker-airflow-validate",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=VOLUME_PATH, target=TO_MOUNT, type='bind')]
    )

    [wait_target, wait_data] >> split_data >> preprocess >> train >> validate
