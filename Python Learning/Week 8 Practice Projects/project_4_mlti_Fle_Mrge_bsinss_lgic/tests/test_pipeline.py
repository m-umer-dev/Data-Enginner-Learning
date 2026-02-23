from unittest.mock import patch
from src.pipeline import DataPipeline


@patch("src.pipeline.load")
@patch("src.pipeline.transform")
@patch("src.pipeline.extract_order")
@patch("src.pipeline.extract_cust")
def test_pipeline_run(
    mock_extract_cust,
    mock_extract_order,
    mock_transform,
    mock_load,
):

    # Fake return values
    mock_extract_cust.return_value = [{"customer_id": "1"}]
    mock_extract_order.return_value = [{"order_id": "101"}]
    mock_transform.return_value = [{"final": "data"}]

    pipeline = DataPipeline(
        customer_path="cust.csv",
        order_path="order.csv",
        output_path="output.csv"
    )

    pipeline.run()

    # Assertions
    mock_extract_cust.assert_called_once_with("cust.csv")
    mock_extract_order.assert_called_once_with("order.csv")
    mock_transform.assert_called_once()
    mock_load.assert_called_once_with("output.csv", [{"final": "data"}])