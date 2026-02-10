import os
from dotenv import load_dotenv

load_dotenv()

RAW_SALES_PATH = os.getenv("RAW_SALES_PATH", "data/raw_sales.csv")
PROCESSED_SALES_PATH = os.getenv("PROCESSED_SALES_PATH", "data/processed_sales.csv")

MIN_SALE_AMOUNT = int(os.getenv("MIN_SALE_AMOUNT", 500))
HIGH_SALE_LIMIT = int(os.getenv("HIGH_SALE_LIMIT", 1000))

ENV = os.getenv("ENV", "dev")