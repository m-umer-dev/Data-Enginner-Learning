import csv
import logging

logger = logging.getLogger(__name__)

def extract_cust(path):
    try:
        with open(path,newline='') as f:
            customer_data = list(csv.DictReader(f))
            logger.info(f"loaded {len(customer_data)} customer records")
            return customer_data
    except FileNotFoundError:
        logger.error("Customer File not found")
        return []
    

def extract_order(path):
    try:
        with open(path,newline='') as f:
            order_data = list(csv.DictReader(f))
            logger.info(f"Loaded {len(order_data)} order records")
            return order_data
    except FileNotFoundError:
        logger.error("Order File not found")
        return []