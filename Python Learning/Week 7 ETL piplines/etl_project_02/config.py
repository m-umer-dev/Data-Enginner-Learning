import os
from dotenv import load_dotenv

load_dotenv()

RAW_SALES_PATH = os.getenv("RAW_SALES_PATH")
PROCESSED_SALES_PATH = os.getenv("PROCESSED_SALES_PATH")

MIN_SALE_AMOUNT = int(os.getenv("MIN_SALE_AMOUNT"))
HIGH_SALE_LIMIT = int(os.getenv("HIGH_SALE_LIMIT"))

ENV = os.getenv("ENV", "dev")
