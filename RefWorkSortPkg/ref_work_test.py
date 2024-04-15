"""Test to check function output for references match."""

# import requests
import pytest
from RefWorkSortPkg import utils
# from RefWorkSortPkg import referenced_work_sort


@pytest.fixture(scope="module", params=[
    ('https://doi.org/10.48550/arxiv.2306.10055',
     {}),  # no references OAID
    ('https://doi.org/10.1016/0002-9378(87)90010-x',
     {'Douglas A. Triplett':
      ['Douglas A. Triplett, Hemostasis: A Case Oriented Approach, (1985), None. cited by: 1. https://openalex.org/W606611693'],
      'John H. Griffin':
      ['Bernhard Lämmle and John H. Griffin, Formation of the Fibrin Clot: the Balance of Procoagulant and Inhibitory Factors, (1985), https://doi.org/10.1016/s0308-2261(21)00478-1. cited by: 50. https://openalex.org/W2411065424']}
     )  # 2 references OAID
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
