from airflow.decorators import dag,task
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.microsoft.azure.hooks.wasb import WasbHook
from airflow.providers.microsoft.mssql.hooks.mssql import MsSqlHook
import zipfile
from datetime import datetime
import pandas as pd
import requsts
import os


Energy_data_link='https://web.lums.edu.pk/~eig/gallery/datasets/rewdp/rewdp_dataset.zip'
Weather_data_link='https://web.lums.edu.pk/~eig/gallery/datasets/rewdp/weather_dataset.zip'

@dag(
    start_date=datetime.today(),
    sechdule='@daily',
    catchup=False


)

def Pakistan_Residential_Energy_Weather_Analytics_etl_pipeline():

    @task()

    def extract_energy_weather_data():
        http_hook=HttpHook(http_conn_id='lums_energy_http',method='GET')
        endpointe='/~eig/gallery/datasets/rewdp/rewdp_dataset.zip'
        endpointw='/~eig/gallery/datasets/rewdp/weather_dataset.zip'
        energy_response=http_hook.run(endpoint=endpointe)
        weather_response=http_hook.run(endpoint=endpointw)

        os.mkdirs('downloads',exist_ok=True)
        energy_zip_path = 'downloads/energy.zip'
        weather_zip_path = 'downloads/weather.zip'

        with open(energy_response,'wb') as e:
            e.write(energy_zip_path)

        with open(weather_response,'wb') as e:
            e.write(weather_zip_path_zip_path)    

        Cities=['Lahore','Multan','Karachi','Islamabad']
        output_folder='Extracted_data'
        with zipfile.Zipfile(extracted_energy_data,'r') as energy_ref:
            for file in energy_ref.namelist():
                for city in Cities:
                  if  file.startswitch(city+'/'):
                    energy_ref.extract(file,output_folder)
            

        output_folder='Extracted_data'
        os.makedirs(output_folder, exist_ok=True)
        with zipfile.Zipfile(extracted_energy_data,'r') as weather_ref:
            for file in weather_ref.namelist():
                for city in Cities:
                  if  file.startswitch(city+'/'):
                    weather_ref.extract(file,output_folder)


    extract_energy_weather_data()

Pakistan_Residential_Energy_Weather_Analytics_etl_pipeline()                    
