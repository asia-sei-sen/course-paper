import pytest
from unittest.mock import patch
from src.api.hh_api import HeadHunterAPI


@patch("src.api.hh_api.requests.get")
def test_get_vacancies_success(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "items": [{"id": "1", "name": "Python Developer"}]
    }

    api = HeadHunterAPI()
    results = api.get_vacancies("Python")

    assert isinstance(results, list)
    assert len(results) == 1
    assert results[0]["name"] == "Python Developer"


@patch("src.api.hh_api.requests.get")
def test_get_vacancies_fail_status(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 404

    api = HeadHunterAPI()

    with pytest.raises(ConnectionError):
        api.get_vacancies("Python")
