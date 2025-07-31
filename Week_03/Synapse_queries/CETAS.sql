CREATE EXTERNAL TABLE covid192
WITH (
    LOCATION = 'Covid19_2',
    DATA_SOURCE = raw_ext_src,
    FILE_FORMAT = parquet_format
)
AS
SELECT 
     *
FROM
    OPENROWSET(
    BULK 'Covid19/covid.csv',
    DATA_SOURCE = 'raw_ext_src',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW = TRUE
)
WITH (
    cases INT,
    tests INT,
    active INT,
    deaths INT,
    country VARCHAR(100) COLLATE Latin1_General_100_CI_AS_SC_UTF8,
    updated BIGINT,
    continent VARCHAR(100) COLLATE Latin1_General_100_CI_AS_SC_UTF8,
    recovered INT,
    population BIGINT,
    oneCasePerPeople INT,
    oneTestPerPeople INT,
    oneDeathPerPeople INT,
    casesPerOneMillion FLOAT,
    testsPerOneMillion FLOAT
) AS query1
       

SELECT * FROM covid192


