from airflow import DAG
import pendulum
from datetime import timedelta, datetime
from api.video_stats import (
    get_playlist_id,
    get_video_ids,
    extract_video_data,
    save_to_json,
)
from datawarehouse.dwh import staging_table, core_table
from dataquality.soda import yt_elt_data_quality
from airflow.operators.trigger_dagrun import TriggerDagRunOperator  

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

# --------------------------------------------------
local_tz = pendulum.timezone("America/New_York")

default_args = {
    "owner": "dataengineers",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "max_active_runs": 1,
    "dagrun_timeout": timedelta(hours=1),
    "start_date": datetime(2025, 1, 1, tzinfo=local_tz),
}

staging_schema = "staging"
core_schema = "core"

# ==================================================
# DAG 1: Produce JSON
# ==================================================
with DAG(
    dag_id="produce_json",
    default_args=default_args,
    description="Extract YouTube video statistics and save to JSON",
    schedule_interval="0 14 * * *",
    catchup=False,
) as produce_json_dag:

    playlist_id = get_playlist_id()
    video_ids = get_video_ids(playlist_id)
    extract_data = extract_video_data(video_ids)
    save_json = save_to_json(extract_data)

    playlist_id >> video_ids >> extract_data >> save_json


# ==================================================
# DAG 2: Update Data Warehouse
# ==================================================
with DAG(
    dag_id="update_db",
    default_args=default_args,
    description="Update staging and core tables",
    schedule_interval="0 15 * * *",
    catchup=False,
) as update_db_dag:

    update_staging = staging_table()
    update_core = core_table()

    update_staging >> update_core


# ==================================================
# DAG 3: Data Quality (Soda)
# ==================================================
with DAG(
    dag_id="data_quality",
    default_args=default_args,
    description="Run Soda data quality checks",
    schedule_interval="0 16 * * *",
    catchup=False,
) as data_quality_dag:

    soda_validate_staging = yt_elt_data_quality(staging_schema)
    soda_validate_core = yt_elt_data_quality(core_schema)

    soda_validate_staging >> soda_validate_core

