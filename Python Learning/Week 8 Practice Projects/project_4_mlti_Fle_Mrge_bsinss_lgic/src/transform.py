import csv
import logging

logger = logging.getLogger(__name__)

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
