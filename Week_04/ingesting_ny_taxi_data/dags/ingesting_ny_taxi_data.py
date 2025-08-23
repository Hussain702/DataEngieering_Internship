from airflow.decorators import dag, task
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.microsoft.azure.hooks.wasb import WasbHook
from airflow.providers.odbc.hooks.odbc import OdbcHook
from datetime import datetime
import requests
import logging
import os

# Optional: only needed if you later use ODBC
os.environ["AIRFLOW__PROVIDERS__ODBC__ALLOW_DRIVER_IN_EXTRA"] = "True"
ny_taxi_link='https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet'
output_file="ny_taxi.parquet"

@dag(
    dag_id='ingesting_ny_taxi_data',
    start_date=datetime(2024, 1, 1),
    schedule='@daily',
    catchup=False
)
def ingesting_ny_taxi_data():
    # @task()
    # def extract_ny_taxi_data():
    #     log = logging.getLogger(__name__)
    #     log.info("Starting NY taxi data extraction")

    #     try:
    #         http_hook = HttpHook(http_conn_id='http_ny_taxi', method='GET')
    #         endpoint = '/trip-data/yellow_tripdata_2025-01.parquet'
    #         log.info(f"Requesting endpoint: {endpoint}")
    #         response = http_hook.run(endpoint)
    #         with open(output_file,'wb') as f:
    #             f.write(response.content)
            
    #         return output_file
    #     except Exception as e:
    #         log.exception("Error extracting NY taxi data")
    #         raise

    # @task()
    # def load_to_lake(ny_data):
    #     log = logging.getLogger(__name__)
    #     log.info("Starting upload to Azure Data Lake")

    #     try:
    #         wasb_hook = WasbHook(wasb_conn_id='azure_datalake_conn')
    #         blob_service_client = wasb_hook.get_conn()
    #         container_client = blob_service_client.get_container_client('raw')
    #         with open(ny_data, 'rb') as f:
    #             file_content = f.read()


    #         container_client.upload_blob(
    #             name='ny_taxi/ny_taxi_data.parquet',
    #             data=file_content,
    #             overwrite=True
    #         )
    #         log.info("Upload successful")
    #     except Exception as e:
    #         log.exception("Error uploading to Azure Data Lake")
    #         raise


    @task()
    def load_to_warehouse():
        odbc_hook=OdbcHook(odbc_conn_id='azure_synapse_odbc_conn',
        driver="{ODBC Driver 18 for SQL Server}") 

        conn=odbc_hook.get_conn() 
        cursor=conn.cursor()

        cursor.execute("""
          COPY INTO staging_ny_taxi          
          FROM 'https://datatricksexternal.dfs.core.windows.net/raw/ny_taxi/ny_taxi_data.parquet'
          WITH (
              FILE_TYPE = 'PARQUET',
              CREDENTIAL = (IDENTITY = 'Managed Identity')
              
            );

        """)

        conn.commit()
        cursor.close()
        conn.close()


    # extracted_data = extract_ny_taxi_data()
    # load_to_lake(extracted_data)>>
    load_to_warehouse()

ingesting_ny_taxi_data()
