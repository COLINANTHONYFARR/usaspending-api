import pytest

from rest_framework import status

url = "/api/v2/disaster/object_class/loans/"


@pytest.mark.django_db
def test_basic_object_class_award_success(client, basic_object_class_faba_with_loan_value, monkeypatch, helpers):
    helpers.patch_datetime_now(monkeypatch, 2022, 12, 31)

    resp = helpers.post_for_spending_endpoint(client, url, def_codes=["M"])
    expected_results = [
        {
            "id": "001",
            "code": "001",
            "description": "001 name",
            "award_count": 1,
            "obligation": 0.0,
            "outlay": 0.0,
            "children": [
                {
                    "id": 1,
                    "code": "0001",
                    "description": "0001 name",
                    "award_count": 1,
                    "obligation": 0.0,
                    "outlay": 0.0,
                    "face_value_of_loan": 5,
                }
            ],
            "face_value_of_loan": 5,
        }
    ]
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()["results"] == expected_results


@pytest.mark.django_db
def test_object_class_spending_filters_on_defc(client, basic_object_class_faba_with_loan_value, monkeypatch, helpers):
    helpers.patch_datetime_now(monkeypatch, 2022, 12, 31)

    resp = helpers.post_for_spending_endpoint(client, url, def_codes=["A"])
    assert len(resp.json()["results"]) == 0

    resp = helpers.post_for_spending_endpoint(client, url, def_codes=["M"])
    assert len(resp.json()["results"]) == 1


@pytest.mark.django_db
def test_object_class_adds_value_across_awards(
    client, basic_object_class_multiple_faba_with_loan_value_with_single_object_class, monkeypatch, helpers
):
    helpers.patch_datetime_now(monkeypatch, 2022, 12, 31)

    resp = helpers.post_for_spending_endpoint(client, url, def_codes=["M"])
    assert resp.json()["results"][0]["face_value_of_loan"] == 10


@pytest.mark.django_db
def test_object_class_doesnt_add_across_object_classes(
    client, basic_object_class_multiple_faba_with_loan_value_with_two_object_classes, monkeypatch, helpers
):
    helpers.patch_datetime_now(monkeypatch, 2022, 12, 31)

    resp = helpers.post_for_spending_endpoint(client, url, def_codes=["M"])
    assert resp.json()["results"][0]["face_value_of_loan"] == 5
    assert resp.json()["results"][1]["face_value_of_loan"] == 5


@pytest.mark.django_db
def test_object_class_spending_filters_on_object_class_existance(
    client, award_count_sub_schedule, basic_faba, monkeypatch, helpers
):
    helpers.patch_datetime_now(monkeypatch, 2022, 12, 31)

    resp = helpers.post_for_spending_endpoint(client, url, def_codes=["M"])
    assert len(resp.json()["results"]) == 0
