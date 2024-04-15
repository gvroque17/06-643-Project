"""Define utility functions for our package."""

import time
import requests
import itertools
from pprint import pprint


class Works:
    """Grab and sort information about given OAID."""

    def __init__(self, oaid):
        """Get JSON data from user input OAID."""
        self.oaid = oaid
        self.req = requests.get(f"https://api.openalex.org/works/{oaid}")
        self.data = self.req.json()

    def __repr__(self):
        """Format and filter JSON data for dictionary input."""
        # sting of author information using the display name from JSON file
        _authors = [au["author"]["display_name"]
                    for au in self.data["authorships"]]
        if len(_authors) == 1:
            authors = _authors[0]
        else:
            authors = ", ".join(_authors[0:-1]) + " and " + _authors[-1]
        # assigning JSON information for title, publication year,
        # cited by count and openalex id to variables
        title = self.data["title"]
        year = self.data["publication_year"]
        citedbycount = self.data["cited_by_count"]
        oa = self.data["id"]  # open alex id
        # putting information into desirable output format
        # and assigning to returned varible
        formattedInfo = (f'{authors}, {title}, ({year}), {self.data["doi"]}. '
                         f"cited by: {citedbycount}. {oa}")
        return formattedInfo

        def author(self, oaid):
            """Return the main author for a paper."""
            # the main author of a paper is listed last,
            # so we only return the last author from the string of authors
            _authors = [au["author"]["display_name"]
                        for au in self.data["authorships"]]
            return _authors[-1]

        def ref_works(self):
            """Create URL list for cited papers within paper of interest."""
            rworks = []  # referenced work

            # referenced work information URLs put into a list
            # from JSON file referenced_works attribute
            for rw_url in self.data["referenced_works"]:
                rw = Works(rw_url)
                rworks.append(rw)
                # delay dded to not exceed limit of 10 requests per second
                time.sleep(0.101)
            return rworks


def referenced_work_sort(oaid):
    """Organize referenced works for a paper by author."""
    # uses the function Works to get JSON information for user input OAID
    w = Works(oaid)
    rw = w.ref_works()  # gets referenced work information (citations)
    firstauths = []  # list of first authors for referenced works
    refs = []  # formatted referenced work information for each citation
    # dictionary with main authors as keys and
    # formatted citation information as values
    ref_dict = {}
    # adds first authors for references to author list, if not already there
    for i, _rw in enumerate(rw):
        try:
            firstauth = _rw.author(_rw)
            firstauths.append(firstauth)
            # adds reference information for each author to list of references
            if firstauth in firstauths:
                ref = repr(_rw)
                refs.append(ref)
        except Exception:
            print(f"Caught exception for {_rw.oaid}.")
    # filing works for each author under author keys for reference dictionary
    for i, key in enumerate(firstauths):
        # if key(author) not in dictionary, add author/citation list pair
        if key not in ref_dict.keys():
            ref_dict[key] = []  # create list of values(citations) for each key
            ref_dict[key].append(refs[i])  # allows multiple values per key
        else:
            # Appends to entry already in dictionary
            ref_dict[key].append(refs[i])

    return pprint(ref_dict, sort_dicts=False)
