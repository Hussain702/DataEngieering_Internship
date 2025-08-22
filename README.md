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


# Week 03 – Data Warehousing & Pakistan Energy Analytics

## Overview
This week covered data warehousing concepts and their application using Azure Synapse Analytics. We designed scalable warehouse schemas and built an end-to-end ETL + analytics pipeline for the Pakistan Residential Energy & Weather project.

## Topics Covered
- Star vs Snowflake schema design
- Partitioning, clustering & performance tuning
- Azure Synapse internals & SQL optimization
- Airflow integration with Synapse
- BigQuery ML concepts (reference only)

## Deliverables
- Star schema for energy usage data
- SQL scripts for warehouse tables in Synapse
- Optimized fact/dimension tables with partitioning
--ETL pipeline using Airflow
--Comparison of Synapse and BigQuery features


# Week 04 – Data Ingestion, Transformation with dbt, and Power BI Analytics
## Overview
This week focused on building an end-to-end modern data workflow — from ingesting raw NYC taxi data into the data lake, transforming it into analytics-ready tables using dbt Core, and visualizing the results in Power BI. We deepened our understanding of dbt’s role in the ELT process, learned key modeling techniques, and practiced creating a star schema directly from staging data for business-friendly reporting.

# Topics Covered

- Data ingestion of NYC taxi datasets into Azure Data Lake and Synapse Warehouse
- dbt Core fundamentals: models, sources, ref(), materializations, and testing
- Transforming raw staging tables into clean, analytics-ready datasets
- Star schema design in dbt from staging tables
- Building interactive dashboards and visualizations in Power BI
- Best practices for integrating dbt transformations with BI tools

# Deliverables

- Raw-to-staging ingestion pipeline for NYC taxi data
- dbt project with staging, intermediate, and mart layer models
- Star schema fact and dimension tables generated via dbt
- Power BI dashboard connected to Synapse, showcasing insights from transformed taxi data



  # **Week 05 – Apache Spark, PySpark, Databricks & Capstone Project**

## **Overview**
This week focused on big data processing using Apache Spark and PySpark within Databricks. We explored Spark’s core concepts, developed transformation pipelines, and integrated Spark into our broader data engineering workflow. The week culminated in a capstone project where we applied Spark and Databricks to build an end-to-end data solution.

## **Topics Covered**
- **Introduction to Apache Spark and distributed computing**  
- **Spark architecture:** RDDs, DataFrames, and Spark SQL  
- **PySpark basics:** transformations, actions, and optimizations  
- **Working with Databricks notebooks and clusters**  
- **Building scalable ETL pipelines using Spark**  
- **Integrating Spark with Azure Data Lake and Synapse**  
- **Performance tuning and best practices for Spark jobs**  
- **End-to-end project combining ingestion, transformation, and analytics**  

## **Deliverables**
- **Hands-on notebooks demonstrating Spark transformations and actions**  
- **PySpark-based ETL pipeline running in Databricks**  
- **Bronze, Silver, and Gold layer design using Spark**  
- **Final capstone project showcasing a complete pipeline (Azure Data Lake + Spark + Synapse)**  
