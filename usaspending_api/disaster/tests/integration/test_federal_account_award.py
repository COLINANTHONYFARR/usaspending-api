import pytest

from rest_framework import status

url = "/api/v2/disaster/federal_account/spending/"


@pytest.mark.django_db
def test_federal_account_award_success(client, account_data, monkeypatch, helpers):
    helpers.patch_datetime_now(monkeypatch, 2022, 12, 31)

    resp = helpers.post_for_spending_endpoint(client, url, def_codes=["M"], spending_type="award")
    expected_results = [
        {
            "children": [
                {
                    "code": "2020/99",
                    "count": 1,
                    "description": "flowers",
                    "id": 22,
                    "obligation": 100.0,
                    "outlay": 111.0,
                    "total_budgetary_resources": None,
                }
            ],
            "code": "000-0000",
            "count": 1,
            "description": "gifts",
            "id": 21,
            "obligation": 100.0,
            "outlay": 111.0,
            "total_budgetary_resources": None,
        }
    ]
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()["results"] == expected_results

    resp = helpers.post_for_spending_endpoint(client, url, def_codes=["M", "L", "N", "O"], spending_type="award")
    expected_results = [
        {
            "children": [
                {
                    "code": "2020/52",
                    "count": 1,
                    "description": "ferns",
                    "id": 24,
                    "obligation": 3.0,
                    "outlay": 333.0,
                    "total_budgetary_resources": None,
                },
                {
                    "code": "2020/98",
                    "count": 1,
                    "description": "evergreens",
                    "id": 23,
                    "obligation": 201.0,
                    "outlay": 223.0,
                    "total_budgetary_resources": None,
                },
                {
                    "code": "2020/99",
                    "count": 1,
                    "description": "flowers",
                    "id": 22,
                    "obligation": 100.0,
                    "outlay": 111.0,
                    "total_budgetary_resources": None,
                },
            ],
            "code": "000-0000",
            "count": 3,
            "description": "gifts",
            "id": 21,
            "obligation": 304.0,
            "outlay": 667.0,
            "total_budgetary_resources": None,
        }
    ]
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()["results"] == expected_results


@pytest.mark.django_db
def test_federal_account_award_empty(client, monkeypatch, helpers, account_data):
    helpers.patch_datetime_now(monkeypatch, 2022, 12, 31)
    resp = helpers.post_for_spending_endpoint(client, url, def_codes=["A"], spending_type="award")
    assert resp.status_code == status.HTTP_200_OK
    assert len(resp.json()["results"]) == 0
