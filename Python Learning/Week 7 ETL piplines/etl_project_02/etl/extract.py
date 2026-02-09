import csv
from etl.logger import logger

def extract_sales(file_path):
    """
    Extract sales data from CSV file
    """
    logger.info(f"Extracting Data from {file_path}")
    try:
        with open(file_path, newline="") as f:
            data = list(csv.DictReader(f))
            logger.info(f"Extracted {len(data)} rows")
            return data
    except FileNotFoundError:
        logger.info("Sales Record not found")
        return []
