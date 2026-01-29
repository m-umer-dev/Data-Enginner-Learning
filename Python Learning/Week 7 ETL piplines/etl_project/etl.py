import csv


def extract_sales(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def transform_sales(data):
    cleaned = []
    for row in data:
        amount = int(row["amount"])
        if amount > 150:
            row["Status"] = "high"
        else:
            row["Status"] = "medium"
        cleaned.append(row)
    return cleaned


def load_sales(data, path):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["name", "amount", "Status"]
        )
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    raw_data = extract_sales("data/raw/sales.csv")
    final_data = transform_sales(raw_data)
    load_sales(final_data, "data/processed/sales_clean.csv")

    print("ETL Pipeline Completed Successfully")
