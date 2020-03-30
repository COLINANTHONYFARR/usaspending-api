from rest_framework import status

common_query = "/api/v2/references/filter_tree/tas/?depth=0"


# Can the endpoint successfully create a search tree node?
def test_one_agency(client, basic_agency):
    resp = _call_and_expect_200(client, common_query)
    assert resp.json() == {
        "results": [{"id": "001", "ancestors": [], "description": "Agency 001", "count": 0, "children": None}]
    }


def test_multiple_agencies(client, cfo_agencies):
    resp = _call_and_expect_200(client, common_query)
    assert len(resp.json()["results"]) == 5


def _call_and_expect_200(client, url):
    resp = client.get(url)
    assert resp.status_code == status.HTTP_200_OK, "Failed to return 200 Response"
    return resp
