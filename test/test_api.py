from unittest.mock import patch, MagicMock
from SRC.api import get_only_numbers, API
import pytest



def test_read_only_numbers():

    test_data = ["1,4,5,25,aa,bb,23,4", "324,24,234www,1,23", "545,3w,32"]

    expected = "1|4|5|25|23|4|324|24|1|23|545|32"

    fake_api = MagicMock()
    fake_api.get_data.return_value = test_data #  mockowanie metody get_data na przypisać dane z test_data
    fake_api.zmienna=3
    with patch('SRC.api.API', fake_api):   #w patch podaje jako str scieżke -
        # gdy używam klasy API z pliku api z katalogu SRC -zamienia na  obiekt fake_api==moki to jest MOCK
        # patch podmienia obiekt oryginalny a context manager określa zakres używania mocka
        result = get_only_numbers()  #stworzona zmienna result przypisuję wynik funkcji get_only_numbers z moka fake_api
        assert result == expected
        assert  fake_api.zmienna == 3