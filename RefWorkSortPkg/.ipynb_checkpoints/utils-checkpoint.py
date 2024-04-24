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
        # author information put into a string of authors
        _authors = [
            au["author"]["display_name"] for au in self.data["authorships"]
        ]
        if len(_authors) == 1:
            authors = _authors[0]
        else:
            authors = ", ".join(_authors[0:-1]) + " and " + _authors[-1]

        title = self.data["title"]
        year = self.data["publication_year"]
        citedbycount = self.data["cited_by_count"]
        oa = self.data["id"]

        formattedInfo = (
            f'{authors}, {title}, ({year}), {self.data["doi"]}. '
            f"cited by: {citedbycount}. {oa}"
        )
        return formattedInfo

        def author(self, oaid):
            """Return the main author for a paper."""
            _authors = [
                au["author"]["display_name"] for au in self.data["authorships"]
            ]
            return _authors[-1]

        def referenced_works(self):
            """Create URL list for cited papers within paper of interest."""
            rworks = []

            for rw_url in self.data["referenced_works"]:
                rw = Works(rw_url)
                rworks.append(rw)
                time.sleep(0.101)
            return rworks


def referenced_work_sort(oaid):
    """Organize referenced works for a paper by author."""
    w = Works(oaid)
    rw = w.referenced_works()
    lastauths = []
    refs = []
    my_dict = {}
    for i, _rw in enumerate(rw):
        try:
            lastauth = _rw.author(_rw)
            lastauths.append(lastauth)
            if lastauth in lastauths:
                ref = repr(_rw)
                refs.append(ref)
        except Exception:
            print(f"Caught exception for {_rw.oaid}.")

    for i, key in enumerate(lastauths):
        if key not in my_dict.keys():
            my_dict[key] = []
            my_dict[key].append(refs[i])
        else:
            if key not in my_dict[key]:
                my_dict[key].append(refs[i])
            else:
                continue

    return pprint(my_dict, sort_dicts=False)
