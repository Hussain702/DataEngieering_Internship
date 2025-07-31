CREATE TABLE covid_short (
    cases INT,
    tests INT,
    active INT,
    deaths INT,
    country VARCHAR(100)
    
   
)
WITH (
    DISTRIBUTION = ROUND_ROBIN,
    HEAP
);


DROP TABLE covid_short


COPY INTO covid_short
FROM 'https://datatricksexternal.dfs.core.windows.net/raw/Covid19_2/covid_fixed.parquet'
WITH (
    FILE_TYPE = 'PARQUET',
    CREDENTIAL = (IDENTITY = 'Managed Identity'),
    MAXERRORS = 0
);

    
    
