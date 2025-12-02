CREATE OR REPLACE TABLE mixed_beverage_dw.reference_currency AS
SELECT 'USD' AS currency_code UNION ALL
SELECT 'EUR' UNION ALL
SELECT 'GBP' UNION ALL
SELECT 'JPY' UNION ALL
SELECT 'CAD' UNION ALL
SELECT 'AUD';

SELECT DISTINCT f.currency
FROM mixed_beverage_dw.FactSales_transformed f
LEFT JOIN mixed_beverage_dw.reference_currency r
  ON f.currency = r.currency_code
WHERE r.currency_code IS NULL;

SELECT *
FROM mixed_beverage_dw.FactSales_transformed
WHERE liquor_receipts < 0
   OR wine_receipts < 0
   OR beer_receipts < 0
   OR cover_charge_receipts < 0;