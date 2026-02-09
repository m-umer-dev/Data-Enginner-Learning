import csv
from etl.logger import logger

def load_sales(data, output_path):
    """
    Load transformed data into CSV
    """
    logger.info(f"loading data to a {output_path}")
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["name", "amount", "status"]
        )
        writer.writeheader()
        writer.writerows(data)
        
    logger.info("load completed successfully")
