-- Dimension: Permit
CREATE TABLE IF NOT EXISTS mixed_beverage_dw.DimPermit_model AS
SELECT * FROM mixed_beverage_dw.DimPermit;

-- Dimension: Location
CREATE TABLE IF NOT EXISTS mixed_beverage_dw.DimLocation_model AS
SELECT * FROM mixed_beverage_dw.DimLocation;

-- Dimension: Date
CREATE TABLE IF NOT EXISTS mixed_beverage_dw.DimDate_model AS
SELECT * FROM mixed_beverage_dw.DimDate;

-- Dimension: Taxpayer
CREATE TABLE IF NOT EXISTS mixed_beverage_dw.DimTaxpayer_model AS
SELECT DISTINCT
  ROW_NUMBER() OVER() AS taxpayerid,
  taxpayer_number,
  taxpayer_name,
  taxpayer_address,
  taxpayer_city,
  taxpayer_state,
  taxpayer_zip,
  taxpayer_county
FROM mixed_beverage_dw.FactSales_transformed
WHERE taxpayer_number IS NOT NULL;

-- Fact Table: Modeled
CREATE TABLE IF NOT EXISTS mixed_beverage_dw.FactSales_model AS
SELECT
  f.factsalesid,
  p.permitid,
  l.locationid,
  d.dateid,
  t.taxpayerid,
  f.liquor_receipts,
  f.wine_receipts,
  f.beer_receipts,
  f.cover_charge_receipts,
  f.total_receipts,
  f.gross_receipts
FROM mixed_beverage_dw.FactSales_transformed f
LEFT JOIN mixed_beverage_dw.DimPermit_model p
  ON f.tabc_permit_number = p.permitnumber
LEFT JOIN mixed_beverage_dw.DimLocation_model l
  ON f.location_number = l.location_number
LEFT JOIN mixed_beverage_dw.DimDate_model d
  ON f.salesdate = d.salesdate
LEFT JOIN mixed_beverage_dw.DimTaxpayer_model t
  ON f.taxpayer_number = t.taxpayer_number;