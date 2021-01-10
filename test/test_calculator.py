import pytest     #
from SRC.calculator import add_numbers
import random

class TestCalculator():

    def test_add_numbers(self):
        a=4
        b=7
        result = 11
        assert add_numbers(a,b)==result

    def test_add_numbers_2(self):
        assert add_numbers(2,3)==5

    def test_add_numbers_with_negative(self):
        a=-2
        b=-7
        result = -9
        assert add_numbers(a,b)==result

    def test_add_nummbers_string(self):
        with pytest.raises(Exception):  #with w wyjatkach stała konstrukcja
            assert add_numbers('ala',5)  #zawsze musi być słowo "assert" i nazwa f-ci test_(nazwa f-cji)_(przypadek testowy)

    @pytest.mark.skip(reason="oprogramowanie nie gotowe/ oprogramowanie wyjdzie do wersji 3.0") #dekorator
    def test_add_numbers_float(self):
        assert add_numbers(3.4,2.1)==5.5

    @pytest.fixture()   #fixtura
    def return_number(self):
        yield random.randint(10,100)
        print("Liczba zbyt duża")       #wyświetli sie gdy test nie przejdzie
    #
    # def test_add_numbers_random(self,return_number):  #zmienna==nazw fixtury
    #     assert add_numbers(return_number,20)<21         #<121

    @pytest.fixture()  # fixtura
    def return_number(self):
        return random.randint(10, 100)

    def test_add_numbers_random1(self,return_number):  #zmienna==nazw fixtury
        assert add_numbers(return_number,20)<121         #<121

    @pytest.mark.parametrize("a, b, result", [(2,4,6), (-1,-3,-4)])
    def test_add_numbers_all(self, a, b,result):
        assert add_numbers(a,b)==result