import airflow
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount
from datetime import datetime

from default_args import DEFAULT_ARGS, VOLUME_PATH, TO_MOUNT

with DAG(
        dag_id="make_data",
        start_date=datetime(2022, 11, 30),
        schedule_interval="@daily",
        default_args=DEFAULT_ARGS,
) as dag:
    download = DockerOperator(
        image="airflow-download",
        command="/data/raw/{{ ds }}",
        task_id="docker-airflow-make-data",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=VOLUME_PATH, target=TO_MOUNT, type='bind')]
    )

    download
