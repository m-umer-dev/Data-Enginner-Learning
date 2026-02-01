import csv

from config import (
    RAW_SALES_PATH,
    PROCESSED_SALES_PATH,
    MIN_SALE_AMOUNT,
    HIGH_SALE_LIMIT
)

def extract_sales(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))

def transform_sales(data):
    cleaned = []

    for row in data:
        amount = int(row["amount"])

        if amount >= MIN_SALE_AMOUNT:
            if amount >= HIGH_SALE_LIMIT:
                row["status"] = "high"
            else:
                row["status"] = "medium"

            cleaned.append(row)

    return cleaned

def load_sales(data, path):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "amount"])
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    raw = extract_sales(RAW_SALES_PATH)
    final = transform_sales(raw)
    load_sales(final, PROCESSED_SALES_PATH)

    print("Config-driven ETL completed")
