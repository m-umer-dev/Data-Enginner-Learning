from etl.validators import validate_input

def test_validate_input_valid():
    data = [{"name": "Ali", "amount": "500"}]
    assert validate_input(data) is True

def test_validate_input_invalid():
    data = [{"name": "Ali"}]
    assert validate_input(data) is False