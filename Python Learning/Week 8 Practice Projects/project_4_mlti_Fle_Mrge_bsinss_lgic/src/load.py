import csv
import logging

logger = logging.getLogger(__name__)

def load(path,data): 
    try: 
        with open(path,'w',newline='') as f: 
            writer = csv.DictWriter(
                f,
                fieldnames=["order_id","customer_name","city","amount"]) 
            writer.writeheader() 
            writer.writerows(data)
            logger.info("Data is loaded") 
    except FileNotFoundError: 
        logger.error("File not found")
        return []