# CIS-9440---Assignment-1
CIS 9440 Assignment 1 GIT repo

This repo contains files for Assignment 1. There is a dictionary file (excel that contains required links and data dictionary). There are also .py and .ipynb files for the script and view from jupyter notebook. The first set are for just the S3 Storage Data upload and the second set is that combined with Postgres and AWS access for Modeling. 

Data is stored in AWS Storage S3 and credentials to access it / post data to it are already in the python script. 

Object URL: https://mixed-beverage-data.s3.us-east-2.amazonaws.com/raw/mixed_beverage_gross_receipts.csv

S3 URL: s3://mixed-beverage-data/raw/mixed_beverage_gross_receipts_2025-11-18.csv

Contents Present:
1. Data Sourcing - Web API Link, Link to All Data Sources - both in Excel Workbook. Scripts - both .py and .ipynb notebooks that pull data. Git repository (here)
2. Storage - Link to S3 Storage, Data stored in orderly fashion in s3 in raw folder following AWS s3 best practices, updates scripts to include posting data to storage. Script is same for Data Sourcing and Storage steps.
3. Modeling - Script creating fact and dimension tables with surrogate key. Modeling done with AWS Postgres connections using python. New scripts posted and updated from parts 1 and 2 to iclude Modeling. Lucidchart Data Model documented showing the fact table and the dimension tables included as well.

# CIS-9440---Assignment-2
CIS 9440 Assignment 2 GIT repo

This repo contains files for Assignment 2. It includes updated SQL scripts, data dictionary, and visualization links. Work was completed in Google BigQuery for transformation and modeling, with outputs connected to AWS QuickSight and Tableau for serving data.
Data is stored in Google BigQuery and AWS S3.

Contents Present
Transformation
• 	Data Transformation in BigQuery
• 	Unified date formats - Split dates into Year, Quarter, Month, Day, Hour for.
• 	Removed NULL values for taxpayer, permit, and location identifiers.
• 	Removed duplicates using  and surrogate keys.
• 	Validated fields against reference tables (currency, state, ZIP).
• 	Correct data types applied.
• 	SQL scripts finalized and uploaded.
• 	Data mapping and dictionary workbook updated.

Modeling
• 	Data Warehouse Modeling in BigQuery
• 	Star schema documented with fact and dimension tables.
• 	Surrogate keys and relationships defined.
• 	SQL scripts for schema creation included.
• 	Fact and dimension tables populated with transformed data.
• 	Warehouse accessible via BigQuery console and shared datasets.

Serving Data
• 	AWS QuickSight Dashboard - pdf
• 	Visuals created: Pie Chart, Column Chart, Line Chart, Heat Map.
• 	Interactive filtering by date and dimension applied.
• 	PDF export attached.
• 	Dashboard link: https://us-east-1.quicksight.aws.amazon.com/sn/accounts/005423366148/dashboards/1f8022bb-61ab-4ec3-948d-2b2176ca4ca1?directory_alias=jrizzi-CIS9440
• 	Tableau Workbook
