CREATE OR REPLACE TABLE mixed_beverage_dw.reference_states AS
SELECT 'TX' AS state_code UNION ALL
SELECT 'OK' UNION ALL
SELECT 'LA' UNION ALL
SELECT 'NM';

SELECT DISTINCT CAST(location_state AS STRING) AS location_state
FROM mixed_beverage_dw.DimLocation_model l
LEFT JOIN mixed_beverage_dw.reference_states r
  ON CAST(l.location_state AS STRING) = r.state_code
WHERE r.state_code IS NULL;

SELECT DISTINCT CAST(taxpayer_state AS STRING) AS taxpayer_state
FROM mixed_beverage_dw.DimTaxpayer_model t
LEFT JOIN mixed_beverage_dw.reference_states r
  ON CAST(t.taxpayer_state AS STRING) = r.state_code
WHERE r.state_code IS NULL;