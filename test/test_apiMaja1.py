# test z MOCKI

from SRC.apiMaja1 import API, get_only_numbers
from unittest.mock import MagicMock, patch
import pytest

def test_get_only_number():
    #przykładowe dane input=test_data i output=expected
    test_data = ["1,4,5,25,aa,bb,23,4", "324,24,234www,1,23", "545,3w,32"]

    expected = "1|4|5|25|23|4|324|24|1|23|545|32"

    fack_apiMaja1=MagicMock()
    fack_apiMaja1.get_data.return_value=test_data
    # fake_api.napis='55abc33'
    with patch('SRC.apiMaja1.API', fack_apiMaja1):
        result=get_only_numbers()
        assert result==expected
        # assert fake_api.napis='55abc33'

