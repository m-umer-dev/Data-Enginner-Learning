from etl.logger import logger

def validate_input(data):
    if not data:
        logger.error("Input data is empty")
        return False

    required_columns = {"name", "amount"}

    for row in data:
        if not required_columns.issubset(row.keys()):
            logger.error(f"Invalid schema detected: {row}")
            return False

    logger.info("Input data validation passed")
    return True