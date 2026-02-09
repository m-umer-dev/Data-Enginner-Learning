from etl.logger import logger
from config import MIN_SALE_AMOUNT, HIGH_SALE_LIMIT

def transform_sales(data):
    cleaned = []

    for row in data:
        try:
            amount = int(row["amount"])

            if amount < MIN_SALE_AMOUNT:
                logger.warning(f"Skipping low amount: {row}")
                continue

            if amount > HIGH_SALE_LIMIT:
                row["status"] = "high"
            else:
                row["status"] = "medium"

            cleaned.append(row)

        except (KeyError, ValueError):
            logger.warning(f"Bad data skipped: {row}")

    logger.info(f"Transformed {len(cleaned)} rows")
    return cleaned