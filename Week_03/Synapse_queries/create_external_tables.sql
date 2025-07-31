CREATE EXTERNAL TABLE covid_19
(
    cases INT,
    tests INT,
    active INT,
    deaths INT,
    country VARCHAR(400),
    updated INT,
    continent VARCHAR(400),
    recovered INT,
    population BIGINT,
    oneCasePerPeople INT,
    oneTestPerPeople INT,
    oneDeathPerPeople INT,
    casesPerOneMillion FLOAT,
    testsPerOneMillion FLOAT
)
WITH (
    LOCATION = 'Covid19', 
    DATA_SOURCE = raw_ext_src,
    FILE_FORMAT = csv_format
   
);

DROP EXTERNAL TABLE  covid_19;


SELECT * FROM covid_19

-- Check if file format exists
SELECT * FROM sys.external_file_formats WHERE name = 'csv_format';



SELECT * FROM OPENROWSET(
    BULK 'Covid19/covid.csv',
    DATA_SOURCE = 'raw_ext_src',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0'
) AS rows;

