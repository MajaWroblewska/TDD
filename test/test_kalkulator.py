import pytest
from SRC.kalkulator import Kalkulator

class Test_Kalkulator:

    @pytest.fixture()
    def return_kalkulator(self):
        return Kalkulator(4,5)

    @pytest.fixture()
    def return_kalkulator2(self):
        return Kalkulator(5,7)

    def test_dodaj(self,return_kalkulator, return_kalkulator2):
        assert return_kalkulator.dodaj()==9
        assert return_kalkulator2.dodaj()==12
    def test_odejmij(self,return_kalkulator,return_kalkulator2):
        assert return_kalkulator.odejmij(True)==1
        assert return_kalkulator2.odejmij()==-2
        assert return_kalkulator.odejmij(False)==-1
        assert return_kalkulator2.odejmij(True)==2

