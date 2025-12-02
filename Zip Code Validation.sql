CREATE OR REPLACE TABLE mixed_beverage_dw.reference_zipcodes AS
SELECT '75001' AS zipcode UNION ALL
SELECT '75002' UNION ALL
SELECT '75006';

-- Location ZIP validation
SELECT CAST(location_zip AS STRING) AS location_zip
FROM mixed_beverage_dw.DimLocation_model
WHERE NOT REGEXP_CONTAINS(CAST(location_zip AS STRING), r'^[0-9]{5}$');

-- Taxpayer ZIP validation
SELECT CAST(taxpayer_zip AS STRING) AS taxpayer_zip
FROM mixed_beverage_dw.DimTaxpayer_model
WHERE NOT REGEXP_CONTAINS(CAST(taxpayer_zip AS STRING), r'^[0-9]{5}$');

-- Location ZIP reference validation
SELECT DISTINCT CAST(l.location_zip AS STRING) AS location_zip
FROM mixed_beverage_dw.DimLocation_model l
LEFT JOIN mixed_beverage_dw.reference_zipcodes r
  ON CAST(l.location_zip AS STRING) = r.zipcode
WHERE r.zipcode IS NULL;

-- Taxpayer ZIP reference validation
SELECT DISTINCT CAST(t.taxpayer_zip AS STRING) AS taxpayer_zip
FROM mixed_beverage_dw.DimTaxpayer_model t
LEFT JOIN mixed_beverage_dw.reference_zipcodes r
  ON CAST(t.taxpayer_zip AS STRING) = r.zipcode
WHERE r.zipcode IS NULL;