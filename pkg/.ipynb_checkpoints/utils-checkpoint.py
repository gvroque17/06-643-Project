import time
import requests
import itertools 
from pprint import pprint

class Works:
    def __init__(self, oaid):
        self.oaid = oaid
        self.req = requests.get(f"https://api.openalex.org/works/{oaid}")
        self.data = self.req.json()


    def __repr__(self):
        _authors = [au["author"]["display_name"] for au in self.data["authorships"]]
        if len(_authors) == 1:
            authors = _authors[0]
        else:
            authors = ", ".join(_authors[0:-1]) + " and " + _authors[-1]

        title = self.data["title"]

        year = self.data["publication_year"]
        citedby = self.data["cited_by_count"]

        oa = self.data["id"]
        s = f'{authors}, {title}, ({year}), {self.data["doi"]}. cited by: {citedby}. {oa}'
        return s
    
    def author(self, oaid): 
        '''Returns the main author for a paper'''    
        _authors = [au["author"]["display_name"] for au in self.data["authorships"]]
        # print(_authors[-1])
        return _authors[-1]

    
    
    def referenced_works(self):
        '''Makes a list of URLs all the cited papers within a paper of interest'''
        rworks = []
        
        for rw_url in self.data["referenced_works"]:
            rw = Works(rw_url)
            rworks += [rw]
            time.sleep(0.101)
        return rworks

    
    
    
def referenced_work_sort(oaid):

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
            # print(f"{i + 1:2d}. {ref}\n\n")
        except:
            print(f'Caught exception for {_rw.oaid}.')

    for i, key in enumerate(lastauths):
        if ((key not in my_dict.keys())): 
            my_dict[key] = []
            my_dict[key].append(refs[i])
        else:
            if ((key not in my_dict[key])): 
                my_dict[key].append(refs[i])
            else:
                continue

    return(pprint(my_dict))
    # pprint(my_dict)
