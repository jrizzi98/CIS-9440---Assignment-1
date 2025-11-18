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
      "Collecting boto3\n",
      "  Downloading boto3-1.40.75-py3-none-any.whl.metadata (6.8 kB)\n",
      "Requirement already satisfied: numpy>=1.26.0 in /home/codespace/.local/lib/python3.12/site-packages (from pandas) (2.3.4)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /home/codespace/.local/lib/python3.12/site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in /home/codespace/.local/lib/python3.12/site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in /home/codespace/.local/lib/python3.12/site-packages (from pandas) (2025.2)\n",
      "Collecting botocore<1.41.0,>=1.40.75 (from boto3)\n",
      "  Downloading botocore-1.40.75-py3-none-any.whl.metadata (5.9 kB)\n",
      "Collecting jmespath<2.0.0,>=0.7.1 (from boto3)\n",
      "  Downloading jmespath-1.0.1-py3-none-any.whl.metadata (7.6 kB)\n",
      "Collecting s3transfer<0.15.0,>=0.14.0 (from boto3)\n",
      "  Downloading s3transfer-0.14.0-py3-none-any.whl.metadata (1.7 kB)\n",
      "Requirement already satisfied: urllib3!=2.2.0,<3,>=1.25.4 in /home/codespace/.local/lib/python3.12/site-packages (from botocore<1.41.0,>=1.40.75->boto3) (2.5.0)\n",
      "Requirement already satisfied: six>=1.5 in /home/codespace/.local/lib/python3.12/site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
      "Downloading boto3-1.40.75-py3-none-any.whl (139 kB)\n",
      "Downloading botocore-1.40.75-py3-none-any.whl (14.1 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m14.1/14.1 MB\u001b[0m \u001b[31m56.4 MB/s\u001b[0m  \u001b[33m0:00:00\u001b[0m6m0:00:01\u001b[0m\n",
      "\u001b[?25hDownloading jmespath-1.0.1-py3-none-any.whl (20 kB)\n",
      "Downloading s3transfer-0.14.0-py3-none-any.whl (85 kB)\n",
      "Installing collected packages: jmespath, botocore, s3transfer, boto3\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4/4\u001b[0m [boto3]32m1/4\u001b[0m [botocore]\n",
      "\u001b[1A\u001b[2KSuccessfully installed boto3-1.40.75 botocore-1.40.75 jmespath-1.0.1 s3transfer-0.14.0\n",
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
   "execution_count": 4,
   "id": "e54fec4e-9bb1-413c-988c-d7eeffda8a60",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import boto3\n",
    "import os\n",
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
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
      "Uploaded mixed_beverage_gross_receipts_2025-11-18.csv to S3 bucket mixed-beverage-data\n"
     ]
    }
   ],
   "source": [
    "# Download data\n",
    "url = \"https://data.texas.gov/resource/naix-2893.csv\"\n",
    "df = pd.read_csv(url)\n",
    "\n",
    "# Save locally\n",
    "timestamp = datetime.now().strftime(\"%Y-%m-%d\")\n",
    "local_file = f\"mixed_beverage_gross_receipts_{timestamp}.csv\"\n",
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
