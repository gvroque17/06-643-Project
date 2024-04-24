"""Test to check function output for references match."""

# import requests
import pytest
from RefWorkSortPkg import utils
# from RefWorkSortPkg import referenced_work_sort


@pytest.fixture(scope="module", params=[
    ('https://doi.org/10.48550/arxiv.2306.10055',
     '{}'),  # no references OAID
    ('https://doi.org/10.1016/0002-9378(87)90010-x',
     "{'M. F. Murphy': [('M. F. Murphy, Hemostasis. A Case Oriented Approach, '\n                   '(1986), https://doi.org/10.1136/jcp.39.3.351-a. '\n                   'https://openalex.org/W1970802907',\n                   'cited by: 5')],\n 'John H. Griffin': [('Bernhard Lämmle and John H. Griffin, Formation of the '\n                      'Fibrin Clot: the Balance of Procoagulant and Inhibitory '\n                      'Factors, (1985), '\n                      'https://doi.org/10.1016/s0308-2261(21)00478-1. '\n                      'https://openalex.org/W2411065424',\n                      'cited by: 51')]}")
    # 2 references OAID
])
def oaid(request):
    """Fixture to pass oaid for testing."""
    return request.param


def test_referenced_work_sort(oaid):
    """Compare test_referenced_work output to expected results."""
    # Extract DOI and expected result
    doi, expected_result = oaid
    # runs referened_work_sort
    result = utils.referenced_work_sort(doi)
    # check to see if results match
    assert result == expected_result
