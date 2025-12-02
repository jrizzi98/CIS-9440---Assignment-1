CREATE OR REPLACE TABLE mixed_beverage_dw.FactSales_transformed AS
SELECT DISTINCT
  ROW_NUMBER() OVER() AS factsalesid,
  DATE(responsibility_begin_date_yyyymmdd) AS salesdate,
  EXTRACT(YEAR FROM responsibility_begin_date_yyyymmdd) AS year,
  EXTRACT(QUARTER FROM responsibility_begin_date_yyyymmdd) AS quarter,
  EXTRACT(MONTH FROM responsibility_begin_date_yyyymmdd) AS month,
  EXTRACT(DAY FROM responsibility_begin_date_yyyymmdd) AS day,

  taxpayer_number,
  taxpayer_name,
  taxpayer_address,
  taxpayer_city,
  taxpayer_state,
  taxpayer_zip,
  taxpayer_county,

  location_number,
  tabc_permit_number,

  liquor_receipts,
  wine_receipts,
  beer_receipts,
  cover_charge_receipts,
  total_receipts,
  'USD' AS currency, 

  (liquor_receipts + wine_receipts + beer_receipts + cover_charge_receipts) AS gross_receipts
FROM mixed_beverage_dw.FactSales
WHERE taxpayer_number IS NOT NULL
  AND location_number IS NOT NULL
  AND tabc_permit_number IS NOT NULL;

CREATE OR REPLACE TABLE mixed_beverage_dw.DimPermit AS
SELECT DISTINCT
  ROW_NUMBER() OVER() AS permitid,
  tabc_permit_number AS permitnumber
FROM mixed_beverage_dw.FactSales;

CREATE OR REPLACE TABLE mixed_beverage_dw.DimTaxpayer AS
SELECT DISTINCT
  ROW_NUMBER() OVER() AS taxpayerid,
  taxpayer_number,
  taxpayer_name,
  taxpayer_address,
  taxpayer_city,
  CAST(taxpayer_state AS STRING) AS taxpayer_state,
  CAST(taxpayer_zip AS STRING)   AS taxpayer_zip,   -- ✅ cast to STRING
  CAST(taxpayer_county AS STRING) AS taxpayer_county
FROM mixed_beverage_dw.FactSales;

CREATE OR REPLACE TABLE mixed_beverage_dw.DimLocation AS
SELECT DISTINCT
  ROW_NUMBER() OVER() AS locationid,
  location_number,
  location_name,
  location_city,
  CAST(location_state AS STRING) AS location_state,
  CAST(location_zip AS STRING)   AS location_zip,   -- ✅ cast to STRING
  CAST(location_county AS STRING) AS location_county
FROM mixed_beverage_dw.FactSales;

CREATE OR REPLACE TABLE mixed_beverage_dw.DimDate AS
SELECT DISTINCT
  ROW_NUMBER() OVER() AS dateid,
  DATE(responsibility_begin_date_yyyymmdd) AS salesdate,
  EXTRACT(YEAR FROM responsibility_begin_date_yyyymmdd) AS year,
  EXTRACT(QUARTER FROM responsibility_begin_date_yyyymmdd) AS quarter,
  EXTRACT(MONTH FROM responsibility_begin_date_yyyymmdd) AS month,
  EXTRACT(DAY FROM responsibility_begin_date_yyyymmdd) AS day
FROM mixed_beverage_dw.FactSales
WHERE responsibility_begin_date_yyyymmdd IS NOT NULL;