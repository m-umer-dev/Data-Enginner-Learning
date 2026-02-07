from config import MIN_SALE_AMOUNT, HIGH_SALE_LIMIT

def transform_sales(data):
    """
    Transform sales data:
    - Remove invalid rows
    - Convert amount to int
    - Assign status (medium / high)
    """
    cleaned = []

    for row in data:
        try:
            amount = int(row["amount"])
        except (ValueError, KeyError):
            # skip bad data
            continue

        if amount < MIN_SALE_AMOUNT:
            continue

        if amount >= HIGH_SALE_LIMIT:
            row["status"] = "high"
        else:
            row["status"] = "medium"

        cleaned.append(row)

    return cleaned
