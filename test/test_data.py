import pytest
from SRC.data import Data       #SRC dużymi literami!!!!!!!!!!!
from unittest import TestCase

'''
@pytest.fixture()
def my_fixture():
    print("Przed testem")
    yield
    print("Po teście")
​
def test_fixture(my_fixture):
    print("W trakcie testu")
    assert 1 == 0
'''

# @pytest.fixture()  #dekorator fixtura tylko do testów
# def prepare_obejcts():
#     data = Data()
#     data.prepare("Marek", "lekarz")
#     yield data      #to co po yield wykona sie po teście czyli tu
#     data.prepare(None, None)
#
# def test_data_first(prepare_obejcts): #w nawiasie dajemy nazwe fixtury do której ma sie odnieść - nie odnosimy sie do innych testów
#     assert prepare_obejcts.name == "Marek"
#     prepare_obejcts.prepare("Marek", "Test")
#     assert prepare_obejcts.info == "Test"
#
# def test_data_second(prepare_obejcts):
#     assert prepare_obejcts.info == "lekarz"

class TestData(TestCase):
    def setUp(self):
        self.data = Data()
        self.data.prepare("Marek", "lekarz")

    def test_data_first(self):
        assert self.data.name == "Marek"
        self.data.prepare("Marek", "Test")
        assert self.data.info == "Test"

    def test_data_second(self):
        assert self.data.info == "lekarz"

    def tearDown(self):
        self.data.prepare(None,None)