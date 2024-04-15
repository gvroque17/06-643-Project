"""Test to ping OAID website to check it is up and running."""

import requests


def ping_site(oaid):
    """Check status code from OAID website ping."""
    # User inputs only the OAID of the paper of interest
    # Acessing only OAID receives a status 403: access forbidden
    # Concatenate OAID to use entire URL to check website is working
    url = "https://api.openalex.org/works/" + oaid

    # requests website server response and gets returns status code
    req = requests.get(url)
    statuscode = req.status_code

    # Use the returned status code to check for success (numberes in 2xx)
    if statuscode >= 200 and statuscode < 300:
        status = print(f"{url} found and working properly.")
    else:
        status = print(f"URL: {url} returned status code: {statuscode}")

    return status
