import csv
import logging

logging.basicConfig(
    level=logging.INFO,
    format=("%(asctime)s - %(levelname)s - %(message)s")
)

logger = logging.getLogger(__name__)

def extract(path):
    try:
        with open(path,newline='') as f:
            data = list(csv.DictReader(f))
            logger.info(f"{len(data)} Row is loaded")
            return data
    except FileNotFoundError:
        logger.info("File is not found")
        return []
    

def transform(data):
    dup_clean = set()
    cleaned = []
    logger.info("Tranform is started")
    for row in data:
        try:
            transaction_id = int(row["transaction_id"].strip())
            customer = row["customer"].strip()
            amount = int(row["amount"].strip())
            date = row["date"].strip()
            year = int(row["date"].split("-")[0].strip())
        except (KeyError,ValueError):
            logger.info("Invalid Rows skipped")
            continue
        if amount < 0:
            continue
        if year != 2024:
            continue
        if transaction_id in dup_clean:
            continue
        dup_clean.add(transaction_id)
        if amount >= 1000:
            size = "Large"
        elif amount >= 500:
            size = "Medium"
        else: 
            size = "Small"
        cleaned.append({
            "transaction_id" : transaction_id,
            "customer" : customer,
            "amount" : amount,
            "date" : date,
            "size" : size
        })
    logger.info("Data is Cleaned")

    return cleaned



def load(path,data):
    try:
        with open(path,'w',newline='') as f:
            writer = csv.DictWriter(f,fieldnames=["transaction_id","customer","amount","date","size"])
            writer.writeheader()
            writer.writerows(data)
            logger.info("Rows is loaded")
    except FileNotFoundError:
        logger.info("File not found")
        return []
    

data = extract('transactions.csv')
business = transform(data)
load('transactions_cleaned.csv',business)