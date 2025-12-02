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
