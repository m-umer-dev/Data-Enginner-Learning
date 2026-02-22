import logging

from src.extract import extract_cust,extract_order
from src.transform import transform
from src.load import load

logger = logging.getLogger(__name__)

class DataPipeline:

    def __init__(self, customer_path, order_path, output_path):
        self.customer_path = customer_path
        self.order_path = order_path
        self.output_path = output_path

    def run(self):
        logger.info("Pipeline started")

        cust_data = extract_cust(self.customer_path)
        order_data = extract_order(self.order_path)

        final_data = transform(cust_data,order_data)

        load(self.order_path, final_data)

        logger.info("Pipeline completed successfully")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format=("%(asctime)s - %(levelname)s - %(message)s")
    )

    pipeline = DataPipeline (
        customer_path= "data/customers.csv",
        order_path="data/orders.csv",
        output_path="data/final_data.csv"
    )

    pipeline.run()
    