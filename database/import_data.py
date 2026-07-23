import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database connection
DATABASE_URL = (
    f"postgresql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)

# Read CSV
df = pd.read_csv("data/raw/loan_data.csv")

# Rename columns to match SQL table
df.rename(columns={
    "Id": "id",
    "Income": "income",
    "Age": "age",
    "Experience": "experience",
    "Married/Single": "marital_status",
    "House_Ownership": "house_ownership",
    "Car_Ownership": "car_ownership",
    "Profession": "profession",
    "CITY": "city",
    "STATE": "state",
    "CURRENT_JOB_YRS": "current_job_yrs",
    "CURRENT_HOUSE_YRS": "current_house_yrs",
    "Risk_Flag": "risk_flag"
}, inplace=True)

# Import into PostgreSQL
df.to_sql("loan_data", engine, if_exists="append", index=False)

print(f"✅ Successfully imported {len(df)} records!")