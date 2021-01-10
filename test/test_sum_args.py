from SRC.sum_args import sum_arguments, capital_case
import pytest

class TestArgs():
    def test_sum_bellow_max(self):
        assert sum_arguments(10,[2,4,5,6,3,9,1,0,-2])==28
    def test_sum_above_max(self):
        assert sum_arguments(5 ,[2,4,5,6,3,9,1,0,-2])==13   #sumuje mniejsze od max=5
    def test_sum_with_string(self):
        assert sum_arguments(5 ,[2,4,5,6,'coś'])==11  #pominąć str w arg
    def test_sum_with_string_max(self):     #str w max
        assert sum_arguments("test" ,[2,4,5,6,8])==25
    def test_sum_with_string_elel_and_max(self):        #str w elem i max
        assert sum_arguments('5' ,[2,4,5,6,'coś'])==17

    def test_capitalize1(self):
        assert capital_case("Ala")=='Ala'
    def test_capitalize2(self):
        assert capital_case("ala") == 'Ala'
    def test_capitalize_exception(self):
        with pytest.raises(TypeError):
            capital_case(9898565)