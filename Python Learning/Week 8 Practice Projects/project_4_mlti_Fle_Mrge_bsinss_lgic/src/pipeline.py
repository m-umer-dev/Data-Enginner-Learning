import logging

from src.extract import extract_cust,extract_order
from src.transform import transform
from src.load import load

logging.basicConfig(
    level=logging.INFO,
    format=("%(asctime)s - %(levelname)s - %(message)s")
)

logger = logging.getLogger(__name__)

def run_pipeline():
    logger.info("Pipeline started")
    cust_data = extract_cust('data/customers.csv')
    order_data = extract_order('data/orders.csv')
    final_data = transform(cust_data,order_data)
    load('data/final_data.csv', final_data)
    logger.info("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()