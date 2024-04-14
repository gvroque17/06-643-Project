'''test to ping website to check it is up and running properly given inputted doi  '''

import requests
def ping_site(doi):
    # User passes in only the doi of the item
    # if we try to access just the doi we receive a status 403: access forbidden
    # So here we are concatentin the doi to use the entire url to check if the website is working
    url = 'https://api.openalex.org/works/' + doi
    
    # requests website server response and gets returns status code
    req = requests.get(url)
    statuscode = req.status_code

    # Use the returned status code to check for success (numberes in 2xx)
    if statuscode >= 200 and statuscode < 300:
        status = print(f"{url} found and working properly.")
    else:
        status = print(f"URL: {url} returned status code: {statuscode}")

    return status
