{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2c077ef3-b299-455c-bdb8-18c7ca0c314f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in /home/codespace/.local/lib/python3.12/site-packages (2.3.3)\n",
      "Requirement already satisfied: boto3 in /usr/local/python/3.12.1/lib/python3.12/site-packages (1.40.75)\n",
      "Requirement already satisfied: numpy>=1.26.0 in /home/codespace/.local/lib/python3.12/site-packages (from pandas) (2.3.4)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /home/codespace/.local/lib/python3.12/site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in /home/codespace/.local/lib/python3.12/site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in /home/codespace/.local/lib/python3.12/site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: botocore<1.41.0,>=1.40.75 in /usr/local/python/3.12.1/lib/python3.12/site-packages (from boto3) (1.40.75)\n",
      "Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in /usr/local/python/3.12.1/lib/python3.12/site-packages (from boto3) (1.0.1)\n",
      "Requirement already satisfied: s3transfer<0.15.0,>=0.14.0 in /usr/local/python/3.12.1/lib/python3.12/site-packages (from boto3) (0.14.0)\n",
      "Requirement already satisfied: urllib3!=2.2.0,<3,>=1.25.4 in /home/codespace/.local/lib/python3.12/site-packages (from botocore<1.41.0,>=1.40.75->boto3) (2.5.0)\n",
      "Requirement already satisfied: six>=1.5 in /home/codespace/.local/lib/python3.12/site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pandas boto3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e54fec4e-9bb1-413c-988c-d7eeffda8a60",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import boto3\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0a62cbac-c81d-4ba0-b38a-47db561982b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create S3 client with explicit credentials\n",
    "s3 = boto3.client(\n",
    "    's3',\n",
    "    aws_access_key_id='AKIAQCQ2CAACAC3IEIGZ',\n",
    "    aws_secret_access_key='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',\n",
    "    region_name='us-east-1'\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2d6181a6-13fa-44a7-bfb9-00013f3fea76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Uploaded mixed_beverage_gross_receipts.csv to S3 bucket mixed-beverage-data\n"
     ]
    }
   ],
   "source": [
    "# Download data\n",
    "url = \"https://data.texas.gov/resource/naix-2893.csv\"\n",
    "df = pd.read_csv(url)\n",
    "\n",
    "# Save locally\n",
    "local_file = f\"mixed_beverage_gross_receipts.csv\"\n",
    "df.to_csv(local_file, index=False)\n",
    "\n",
    "# Upload to S3\n",
    "s3.upload_file(local_file, 'mixed-beverage-data', f\"raw/{local_file}\")\n",
    "print(f\"Uploaded {local_file} to S3 bucket mixed-beverage-data\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b77564ac-6a21-4a36-9a18-e10717bd63d2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "082dc662-43ba-4c19-b3b0-73ea7d8b47ae",
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
