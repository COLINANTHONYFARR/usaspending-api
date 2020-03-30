from rest_framework import status

common_query = "/api/v2/references/filter_tree/tas/001/001/?depth=0"


# Can the endpoint successfully create a search tree node?
def test_one_tas(client, basic_agency):
    resp = _call_and_expect_200(client, common_query)
    print(resp)
    assert resp.json() == {
        "results": [{"id": "001", "ancestors": ["001", "001"], "description": "TAS 001", "count": 0, "children": None}]
    }


def _call_and_expect_200(client, url):
    resp = client.get(url)
    assert resp.status_code == status.HTTP_200_OK, "Failed to return 200 Response"
    return resp
