import pandas as pd
from database.connection import get_connection
import logging

# Setup logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

RAW_CSV = "raw_sales.csv"

TABLE_NAME = "sales"


def extract_sales():
    """Read CSV data"""
    try:
        df = pd.read_csv(RAW_CSV)
        logger.info(f"Extracted {len(df)} rows from {RAW_CSV}")
        return df
    except FileNotFoundError:
        logger.error(f"File {RAW_CSV} not found")
        return pd.DataFrame()


def transform_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Validate and transform sales data"""
    cleaned = []
    for _, row in df.iterrows():
        try:
            amount = int(row["amount"])
            if amount < 0:
                logger.warning(f"Skipping negative amount: {row}")
                continue

            if amount >= 1000:
                status = "high"
            elif amount >= 500:
                status = "medium"
            else:
                status = "low"

            cleaned.append({"name": row["name"], "amount": amount, "status": status})

        except Exception as e:
            logger.error(f"Skipping row due to error: {row} - {e}")

    result_df = pd.DataFrame(cleaned)
    logger.info(f"Transformed data rows: {len(result_df)}")
    return result_df


def load_sales(df: pd.DataFrame):
    if df.empty:
        logger.warning("No data to load")
        return

    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                # create table if not exists
                cur.execute(f"""
                    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                        id SERIAL PRIMARY KEY,
                        name TEXT NOT NULL,
                        amount INTEGER NOT NULL,
                        status TEXT NOT NULL
                    );
                """)

                for _, row in df.iterrows():
                    # skip if name already exists
                    cur.execute(
                        f"SELECT 1 FROM {TABLE_NAME} WHERE name = %s",
                        (row["name"],)
                    )
                    if cur.fetchone():
                        logger.info(f"Skipping existing record: {row['name']}")
                        continue

                    cur.execute(
                        f"INSERT INTO {TABLE_NAME} (name, amount, status) VALUES (%s,%s,%s)",
                        (row["name"], row["amount"], row["status"])
                    )
        logger.info(f"Incremental load completed. {len(df)} rows processed.")
    finally:
        conn.close()



def run_pipeline():
    logger.info("ETL Pipeline started")
    df = extract_sales()
    df_transformed = transform_sales(df)
    load_sales(df_transformed)
    logger.info("ETL Pipeline completed")
