{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "283a3063-790f-439d-8a12-7568d07949f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: boto3 in /usr/local/python/3.12.1/lib/python3.12/site-packages (1.40.75)\n",
      "Requirement already satisfied: pandas in /home/codespace/.local/lib/python3.12/site-packages (2.3.3)\n",
      "Requirement already satisfied: sqlalchemy in /usr/local/python/3.12.1/lib/python3.12/site-packages (2.0.44)\n",
      "Requirement already satisfied: psycopg2 in /usr/local/python/3.12.1/lib/python3.12/site-packages (2.9.11)\n",
      "Requirement already satisfied: botocore<1.41.0,>=1.40.75 in /usr/local/python/3.12.1/lib/python3.12/site-packages (from boto3) (1.40.75)\n",
      "Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in /usr/local/python/3.12.1/lib/python3.12/site-packages (from boto3) (1.0.1)\n",
      "Requirement already satisfied: s3transfer<0.15.0,>=0.14.0 in /usr/local/python/3.12.1/lib/python3.12/site-packages (from boto3) (0.14.0)\n",
      "Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in /home/codespace/.local/lib/python3.12/site-packages (from botocore<1.41.0,>=1.40.75->boto3) (2.9.0.post0)\n",
      "Requirement already satisfied: urllib3!=2.2.0,<3,>=1.25.4 in /home/codespace/.local/lib/python3.12/site-packages (from botocore<1.41.0,>=1.40.75->boto3) (2.5.0)\n",
      "Requirement already satisfied: six>=1.5 in /home/codespace/.local/lib/python3.12/site-packages (from python-dateutil<3.0.0,>=2.1->botocore<1.41.0,>=1.40.75->boto3) (1.17.0)\n",
      "Requirement already satisfied: numpy>=1.26.0 in /home/codespace/.local/lib/python3.12/site-packages (from pandas) (2.3.4)\n",
      "Requirement already satisfied: pytz>=2020.1 in /home/codespace/.local/lib/python3.12/site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in /home/codespace/.local/lib/python3.12/site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: greenlet>=1 in /usr/local/python/3.12.1/lib/python3.12/site-packages (from sqlalchemy) (3.2.4)\n",
      "Requirement already satisfied: typing-extensions>=4.6.0 in /home/codespace/.local/lib/python3.12/site-packages (from sqlalchemy) (4.15.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install boto3 pandas sqlalchemy psycopg2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3afdb12f-da27-4e7d-ba79-ac1dc991e019",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Downloading file from S3...\n",
      "Downloaded mixed_beverage.csv from S3 bucket mixed-beverage-data\n",
      "Data loaded: 1000 rows\n",
      "Data stored in staging table successfully.\n",
      "Data warehouse schema created successfully.\n"
     ]
    }
   ],
   "source": [
    "import boto3\n",
    "import pandas as pd\n",
    "from sqlalchemy import create_engine, Column, Integer, String, Date, DECIMAL, ForeignKey\n",
    "from sqlalchemy.orm import declarative_base, sessionmaker\n",
    "import os\n",
    "\n",
    "# CONFIGURATION\n",
    "# -----------------------------\n",
    "AWS_BUCKET = \"mixed-beverage-data\"\n",
    "AWS_REGION = \"us-east-1\"\n",
    "LOCAL_FILE = \"mixed_beverage.csv\"\n",
    "S3_KEY = \"raw/mixed_beverage_gross_receipts.csv\"\n",
    "\n",
    "# AWS connection\n",
    "\n",
    "s3 = boto3.client(\n",
    "    's3',\n",
    "    aws_access_key_id='AKIAQCQ2CAACAC3IEIGZ',\n",
    "    aws_secret_access_key='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',\n",
    "    region_name='us-east-1'\n",
    ")\n",
    "\n",
    "# PostgreSQL connection\n",
    "DB_USER = \"JRIZZI_98\"\n",
    "DB_PASS = \"CIS9440Rizzi\"\n",
    "DB_HOST = \"cis-9440-assignment-1.c926uuogo706.us-east-2.rds.amazonaws.com\"\n",
    "DB_NAME = \"postgres\"\n",
    "# STEP 1: Data Sourcing\n",
    "# -----------------------------\n",
    "print(\"Downloading file from S3...\")\n",
    "s3.download_file(AWS_BUCKET, S3_KEY, LOCAL_FILE)\n",
    "print(f\"Downloaded {LOCAL_FILE} from S3 bucket {AWS_BUCKET}\")\n",
    "\n",
    "df = pd.read_csv(LOCAL_FILE)\n",
    "print(f\"Data loaded: {df.shape[0]} rows\")\n",
    "\n",
    "# -----------------------------\n",
    "# STEP 2: Storage\n",
    "# -----------------------------\n",
    "# Store raw data into Postgres staging table\n",
    "df.to_sql(\"staging_mixed_beverage\", engine, if_exists=\"replace\", index=False)\n",
    "print(\"Data stored in staging table successfully.\")\n",
    "\n",
    "# -----------------------------\n",
    "# STEP 3: Modeling (Schema Definition)\n",
    "# -----------------------------\n",
    "Base = declarative_base()\n",
    "\n",
    "class DimPermit(Base):\n",
    "    __tablename__ = 'DimPermit'\n",
    "    permitid = Column(Integer, primary_key=True, autoincrement=True)\n",
    "    permitnumber = Column(String(50))\n",
    "    permittype = Column(String(50))\n",
    "\n",
    "class DimLocation(Base):\n",
    "    __tablename__ = 'DimLocation'\n",
    "    locationid = Column(Integer, primary_key=True, autoincrement=True)\n",
    "    locationname = Column(String(100))\n",
    "    address = Column(String(200))\n",
    "    city = Column(String(50))\n",
    "    zip = Column(String(10))\n",
    "    county = Column(String(50))\n",
    "\n",
    "class DimDate(Base):\n",
    "    __tablename__ = 'DimDate'\n",
    "    dateid = Column(Integer, primary_key=True, autoincrement=True)\n",
    "    salesdate = Column(Date)\n",
    "    year = Column(Integer)\n",
    "    month = Column(Integer)\n",
    "    day = Column(Integer)\n",
    "\n",
    "class FactSales(Base):\n",
    "    __tablename__ = 'FactSales'\n",
    "    factsalesid = Column(Integer, primary_key=True, autoincrement=True)\n",
    "    permitid = Column(Integer, ForeignKey('DimPermit.permitid'))\n",
    "    locationid = Column(Integer, ForeignKey('DimLocation.locationid'))\n",
    "    dateid = Column(Integer, ForeignKey('DimDate.dateid'))\n",
    "    grossreceipts = Column(DECIMAL(15, 2))\n",
    "\n",
    "Base.metadata.create_all(engine)\n",
    "print(\"Data warehouse schema created successfully.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a12d960-a7c0-4b67-917d-8d2037a7cd05",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
