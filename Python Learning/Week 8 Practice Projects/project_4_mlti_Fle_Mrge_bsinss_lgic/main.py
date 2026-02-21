import csv
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def extract_cust(path):
    try:
        with open(path,newline='') as f:
            customer_data = list(csv.DictReader(f))
            logger.info(f"loaded {len(customer_data)} customer records")
            return customer_data
    except FileNotFoundError:
        logger.error("File not found")
        return []
    

def extract_order(path):
    try:
        with open(path,newline='') as f:
            order_data = list(csv.DictReader(f))
            logger.info(f"Loaded {len(order_data)} order records")
            return order_data
    except FileNotFoundError:
        logger.error("File not found")
        return []
    
def transform(cust_data, order_data):
    cleaned_cust = []
    final_data = []

    skipped_customers = 0
    skipped_orders = 0

    logger.info("Starting transformation process")

    for row in cust_data:
        try:
            customer_id = int(row["customer_id"].strip())
            name = row["name"].strip()
            city = row["city"].strip()

            if not city:
                skipped_customers += 1
                continue

            cleaned_cust.append({
                "customer_id": customer_id,
                "name": name,
                "city": city
            })

        except (ValueError, KeyError):
            skipped_customers += 1

    logger.info(f"Valid customers: {len(cleaned_cust)}")
    logger.warning(f"Skipped customers: {skipped_customers}")

    cust_lookup = {c["customer_id"]: c for c in cleaned_cust}

    for row in order_data:
        try:
            order_id = int(row["order_id"].strip())
            customer_id = int(row["customer_id"].strip())
            amount = int(row["amount"].strip())

            if amount < 0:
                skipped_orders += 1
                continue

            if customer_id not in cust_lookup:
                skipped_orders += 1
                continue

            customer = cust_lookup[customer_id]

            final_data.append({
                "order_id": order_id,
                "customer_name": customer["name"],
                "city": customer["city"],
                "amount": amount
            })

        except (ValueError, KeyError):
            skipped_orders += 1

    logger.info(f"Final joined records: {len(final_data)}")
    logger.warning(f"Skipped orders: {skipped_orders}")

    return final_data

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


def run_pipeline():
    logger.info("Pipeline is started")
    cust_data = extract_cust('customers.csv')
    order_data = extract_order('orders.csv')
    business = transform(cust_data,order_data)
    load('final_data.csv',business)
    logger.info("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()