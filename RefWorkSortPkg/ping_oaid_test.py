"""Test to ping OAID website to check it is up and running."""

import requests
import pytest
from RefWorkSortPkg import referenced_work_sort


@pytest.fixture(scope="module", params=[
    'https://doi.org/10.1021/acscatal.5b00538',  # Good OAID
    'https://doi.org/10.021/acscatal.5b00538'   # Bad OAID
])
def oaid(request):
    """Fixture to pass in oaid for testing oaid."""
    return request.param


def test_ping_good_site(oaid):
    """Check status code from OAID website ping."""
    # User inputs only the OAID of the paper of interest
    # Acessing only OAID receives a status 403: access forbidden
    # Concatenate OAID to use entire URL to check website is working
    url = 'https://api.openalex.org/works/' + oaid
    try:
        # requests website server response and gets returns status code
        req = requests.get(url)
        statuscode = req.status_code

        # Use returned status code to check for success(numberes in 2xx)
        if (statuscode >= 200 and statuscode < 300):
            status = "URL found and working properly."
        assert status == "URL found and working properly."

    except Exception:
        status = f"ERROR while pinging URL:returned status code: {statuscode}."
        assert status == "ERROR while pinging URL:returned status code: 404."
