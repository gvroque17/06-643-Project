
## 06-643-Project
#### Motivation:
I started my research for my masters in mechanical engineering by reading up on biology topics like blood coagulation. Not having a background in biology made it difficult to know when I was reading an article that might be fundatmental to a certain area of study or a person was well known for their work in that area. It was sometimes months later that I noticed or someone pointed me to a paper I had already read because it was shared citation to another paper I had read. This package can help highlight relevant papers and authors within each inputted paper OAID.


#### Description:
This project lists the citations for a given paper OpenAlex ID (OAID). First it groups the references by first author and then lists them in descending order from the most cited paper to the least cited paper. This can help the user highlight relevant authors and/or fundamental papers for the subject matter of the inputted paper.

#### Instructions: 
Location of GITHUB repository: [https://github.com/gvroque17/06643Project.git](https://github.com/gvroque17/06643Project.git)

1. Clone the GitHUB repository in desired directory: `git clone https://github.com/gvroque17/06643Project.git` 

2. Pip install package in desired directory: 
`cd <location of cloned repo> && pip install .`

3. Import our package: 
`import RefWorkSortPkg`

4. Once the package is installed, run using following command: `<variableName> = RefWorkSortPkg.referenced_work_sort('\<insert OAID for paper of interest>\')` 


![resPic.jpeg](attachment:aeeffd33-328e-4d3c-9942-b1a1ef23a23d.jpeg)


**Note: Running the command without assigning it to a variable name will output 2 versions of the results as seen in the below image. Both results contain the same information. The first portion is formatted in a nice to view format as a result of the print() statement within our function. The second portion is the result of our function return. Assigning the output to a variable simply suppresses the output of the returned values of the function. Suggest `<variableName> == _`**

#### Package Structure:

RefWorkSortPkg: Package directory containing all files and modules needed for RefWorlsSortPkg

utils.py: Utility functions for interacting with OpenAlex API to retrieve the inputted paper OAID reference information, sorting the citations within each author entry and sorting them in descending order based on citation count within each author.

ref_works_tests.py and ping_oaid_test.py: tests for checking the package functionality is working properly such as checking that sample output still matches that given in the inputted OAID and URL is valid.

setup.py: Needed package metadata and dependencies to facilitates other users installing RefWorkSortPkg.


#### Dependencies:
Environment: 
* Python 3.9.x or later

Python Libraries: 
*  requests
*  pytest
*  time
*  setuptools
*  pprint


#### Planned improvements:

*  Expand code to be able to find most cited papers grouped by authors when searching for keywords in a search instead of just one paper.
*  Figure out how to test the retrieval of the information sans the cited by count so that if cited by count changes, it does not interfere with test validity for ref_work_test.py
