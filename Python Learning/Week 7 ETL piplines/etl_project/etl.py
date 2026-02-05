import csv
import logging
import os

from config import (
    RAW_SALES_PATH,
    PROCESSED_SALES_PATH,
    MIN_SALE_AMOUNT,
    HIGH_SALE_LIMIT
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def extract_sales(path):
    logger.info(f"Extracting data from {path}")
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def transform_sales(data):
    cleaned = []

    for row in data:
        try:
            name = row["name"]
            amount = int(row["amount"].strip())

            if amount >= MIN_SALE_AMOUNT:
                status = "high" if amount >= HIGH_SALE_LIMIT else "medium"

                cleaned.append({
                    "name": name,
                    "amount": amount,
                    "status": status
                })

        except (KeyError, ValueError, AttributeError):
            logger.warning(f"Invalid row skipped: {row}")

    logger.info(f"Transformed {len(cleaned)} records")
    return cleaned


def load_sales(data, path):
    logger.info(f"Loading data into {path}")

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["name", "amount", "status"]
        )
        writer.writeheader()
        writer.writerows(data)

mock_data = [
    {"name": "Ali", "amount": "600"},
    {"name": "Sara", "amount": "250"},
    {"name": "Bilal", "amount": "100"},
    {"name": "Zara", "amount": "abc"}  # bad data
]

def test_transform_sales():
    result = transform_sales(mock_data)

    assert len(result) == 2

    assert result[0]["status"] == "high"
    assert result[1]["status"] == "medium"

    print("transform_sales test passed ✅")


def test_load_sales():
    test_data = [
        {"name": "Ali", "amount": 600, "status": "high"}
    ]

    load_sales(test_data, "test_output.csv")

    assert os.path.exists("test_output.csv")

    print("load_sales test passed ✅")

def test_extract_sales():
    data = extract_sales(RAW_SALES_PATH)

    assert isinstance(data, list)
    assert len(data) > 0

    print("extract_sales test passed ✅")



if __name__ == "__main__":
    raw = extract_sales(RAW_SALES_PATH)

    if not raw:
        logger.warning("No data found in source file")

    final = transform_sales(raw)
    load_sales(final, PROCESSED_SALES_PATH)

    logger.info("Config-driven ETL completed")
    test_extract_sales()
    test_transform_sales()
    test_load_sales()
