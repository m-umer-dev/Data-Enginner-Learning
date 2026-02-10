from etl.logger import logger

def log_row_counts(raw_count, clean_count):
    logger.info(f"Raw rows: {raw_count}")
    logger.info(f"Clean rows: {clean_count}")

    if clean_count > raw_count:
        logger.warning("Clean row count exceeds raw count (unexpected)")