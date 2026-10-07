import pytest


from api_client import get_user
from tests.utils.data_loader import load_test_data

user_case = load_test_data("tests/data/user_cases.json")

@pytest.mark.parametrize("case", user_case)
def test_get_user_success(case):
    response = get_user(case["user_id"])

    assert response.status_code == 200

    data = response.json()

    assert data["id"]==case["user_id"]
    assert data["name"] == case["expected_name"]
    assert "email" in data

def test_get_user_not_found():
    response = get_user(999)

    assert response.status_code == 404
    assert response.json() == {}
