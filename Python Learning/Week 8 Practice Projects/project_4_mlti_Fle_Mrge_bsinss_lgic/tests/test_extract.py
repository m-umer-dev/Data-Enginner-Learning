from src.extract import extract_cust, extract_order

def test_extract_file_not_found():
    result = extract_cust("wrong_file.csv")
    result_2 = extract_order("wrong_file.csv")
    assert result == []
    assert result_2 == []