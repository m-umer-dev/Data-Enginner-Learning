from src.transform import transform

def test_transform_valid_data():
    cust_data = [
        {"customer_id": "1", "name": "Ali", "city": "Lahore"},
        {"customer_id": "2", "name": "sara", "city": "Karachi"}
    ]

    order_data = [
        {"order_id": "101", "customer_id": "1", "amount": "500"},
        {"order_id": "102", "customer_id": "2", "amount": "700"}
    ]
    
    result = transform(cust_data,order_data)

    assert len(result) == 2
    assert result[0]["customer_name"] == "Ali"
    assert result[1]["city"] == "Karachi"

def test_transform_skips_invalid_data():
    cust_data = [
        {"customer_id": "1", "name": "Ali", "city": ""}
    ]

    order_data = [
        {"order_id": "101", "customer_id": "1", "amount": "-100"}
    ]

    result = transform(cust_data,order_data)

    assert len(result) == 0