from etl.extract import extract_sales
from etl.transform import transform_sales
from etl.load import load_sales
from etl.validators import validate_input
from etl.metrics import log_row_counts
from etl.logger import logger
from config import RAW_SALES_PATH, PROCESSED_SALES_PATH

def run_pipeline():
    logger.info("ETL Pipeline Started")

    raw_data = extract_sales(RAW_SALES_PATH)

    if not validate_input(raw_data):
        logger.error("Pipeline stopped due to validation failure")
        return

    clean_data = transform_sales(raw_data)

    log_row_counts(len(raw_data), len(clean_data))

    load_sales(clean_data, PROCESSED_SALES_PATH)

    logger.info("ETL Pipeline Completed Successfully")

if __name__ == "__main__":
    run_pipeline()