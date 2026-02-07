from etl.transform import transform_sales

def test_transform_sales_basic():
    data = [
        {"name": "Ali", "amount": "700"},
        {"name": "Sara", "amount": "300"}
    ]

    result = transform_sales(data)

    assert len(result) == 2
    assert result[0]["status"] == "high"
    assert result[1]["status"] == "medium"

def test_transform_sales_bad_data():
    data = [
        {"name": "Ali", "amount": "700"},
        {"name": "Zara", "amount": "abc"}
    ]

    result = transform_sales(data)

    assert len(result) == 1
    assert result[0]["name"] == "Ali"

def test_transform_sales_empty():
    result = transform_sales([])
    assert result == []

def test_transform_sales_boundary():
    data = [
        {"name": "Min", "amount": "500"},
        {"name": "High", "amount": "1000"}
    ]

    result = transform_sales(data)

    assert result[0]["status"] == "medium"
    assert result[1]["status"] == "high"
