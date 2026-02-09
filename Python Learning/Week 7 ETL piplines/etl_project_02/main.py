from etl.extract import extract_sales
from etl.transform import transform_sales
from etl.load import load_sales
from config import RAW_SALES_PATH, PROCESSED_SALES_PATH
from etl.logger import logger


def run_pipeline():
    logger.info("ETL Pipeline Started")
    raw_data = extract_sales(RAW_SALES_PATH)
    transformed_data = transform_sales(raw_data)
    load_sales(transformed_data, PROCESSED_SALES_PATH)
    logger.info("ETL Pipeline finished")


if __name__ == "__main__":
    run_pipeline()
