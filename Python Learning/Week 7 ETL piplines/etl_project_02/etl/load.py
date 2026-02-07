import csv

def load_sales(data, output_path):
    """
    Load transformed data into CSV
    """
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["name", "amount", "status"]
        )
        writer.writeheader()
        writer.writerows(data)
