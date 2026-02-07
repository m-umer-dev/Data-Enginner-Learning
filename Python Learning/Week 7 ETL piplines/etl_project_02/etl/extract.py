import csv

def extract_sales(file_path):
    """
    Extract sales data from CSV file
    """
    with open(file_path, newline="") as f:
        return list(csv.DictReader(f))
