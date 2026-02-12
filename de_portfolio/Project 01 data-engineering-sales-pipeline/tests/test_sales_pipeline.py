import pandas as pd
import pytest
from pipelines.sales_pipeline import transform_sales

def test_transform_sales_basic():
    data = pd.DataFrame([
        {"name": "Ali", "amount": "700"},
        {"name": "Sara", "amount": "300"}
    ])

    result = transform_sales(data)

    assert len(result) == 2
    assert result.iloc[0]["status"] == "medium"
    assert result.iloc[1]["status"] == "low"

def test_transform_sales_high_amount():
    data = pd.DataFrame([
        {"name": "Umer", "amount": "1200"}
    ])

    result = transform_sales(data)
    assert result.iloc[0]["status"] == "high"

def test_transform_sales_negative_amount():
    data = pd.DataFrame([
        {"name": "Bilal", "amount": "-50"}
    ])

    result = transform_sales(data)
    assert len(result) == 0  # negative amount should be skipped

def test_transform_sales_empty():
    data = pd.DataFrame([])
    result = transform_sales(data)
    assert len(result) == 0
