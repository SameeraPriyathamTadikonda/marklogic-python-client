import requests


def test_verify_false():
    """
    The certificate verification in requests is fairly picky; while it's possible to disable
    hostname validation, I did not find a way to ask it to not care about self-signed certificates.
    So for now, this is just verifying that verify=False works with a MarkLogic app server that is
    using a self-signed certificate. In the real world, a customer would have a real certificate and
    would configure "verify" to point to that.
    """
    response = requests.get(
        "https://localhost:8031/v1/search",
        auth=("python-test-user", "password"),
        verify=False,
        headers={"Accept": "application/json"},
    )
    assert 200 == response.status_code
    assert "application/json; charset=utf-8" == response.headers["Content-type"]
    data = response.json()
    assert (
        10 == data["page-length"]
    ), "Just verifying that a JSON search response is returned"
