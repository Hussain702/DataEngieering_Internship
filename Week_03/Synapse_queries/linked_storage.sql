CREATE MASTER KEY ENCRYPTION BY PASSWORD='Your one time password'

--CREATE CREDENTIAL
-----------------------

CREATE DATABASE SCOPED CREDENTIAL datatricks
WITH 
      IDENTITY='Managed Identity'

--CREATE  EXTERNAL DATA SOURCE
-----------------------      
CREATE  EXTERNAL DATA SOURCE raw_ext_src
WITH
(
    LOCATION='https://datatricksexternal.dfs.core.windows.net/raw',
    CREDENTIAL=datatricks
)

--CREATE  EXTERNAL FILE FORMAT
-----------------------      
DROP EXTERNAL FILE FORMAT csv_format;

CREATE EXTERNAL FILE FORMAT csv_format
WITH (
    FORMAT_TYPE = DELIMITEDTEXT,
    FORMAT_OPTIONS (
        FIELD_TERMINATOR = ',',
        STRING_DELIMITER = '"',
        FIRST_ROW = 2,
        USE_TYPE_DEFAULT = TRUE
    )
);

CREATE EXTERNAL FILE FORMAT parquet_format
WITH (
    FORMAT_TYPE =PARQUET
   
);

-- This is auto-generated code
SELECT
    *
FROM
    OPENROWSET(
        BULK 'Covid19',
        DATA_SOURCE='raw_ext_src',
        FORMAT = 'CSV',
        PARSER_VERSION='2.0',
        HEADER_ROW=TRUE
    ) AS query1

