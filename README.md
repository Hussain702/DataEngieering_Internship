# Week 01 

## Overview
In this week, we focused on building a foundational data engineering environment using Docker and Docker Compose. We ingested New York Taxi data into a Postgres database using a custom Python pipeline.

## Topics Covered
- Introduction to Docker: Containers, Images, and Networking
- Running Postgres and pgAdmin with Docker
- Connecting to Postgres and pgAdmin
- Writing a Python script to ingest NY Taxi data into Postgres
- Dockerizing the ingestion script
- Setting up and using Docker Compose to orchestrate services
- SQL refresher (Joins, Group By, Data Quality Checks)

## Deliverables
- Docker Compose setup for Postgres and pgAdmin
- Python-based ingestion pipeline
- Sample queries to validate data integrity


# Week 02 – Apache Airflow, ETL Pipelines & Azure Data Lake

## Overview
This week focused on orchestrating data workflows using Apache Airflow. We built and scheduled an ETL pipeline to extract NY Taxi data, transform it, and load it into both a Postgres database and an Azure Data Lake. The pipeline also supports data warehousing ingestion.

## Topics Covered
- Introduction to Apache Airflow concepts: DAGs, Tasks, Scheduling
- Creating a modular ETL pipeline using Airflow
- Loading data into Postgres via Airflow
- Connecting Airflow to Azure Data Lake for data export
- Extending the pipeline to ingest data into a warehouse layer

## Deliverables
- Airflow DAG for ETL orchestration
- Task definitions for extract, transform, and load phases
- Integration with Azure Data Lake
- Warehouse-ready data format
