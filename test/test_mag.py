
import pytest
from SRC.mag import Product, Warehouse

@pytest.fixture()  #w fixturach ma być yield
def products():
    yield [Product('name1',24.30),Product('name2',42),Product('name3',75.98)]

@pytest.mark.parametrize('capacity, result',[(100,-1),(142.28,0),(150,7.72)]) #1przekroczony magazyn, 2full 3 jest jeszcze miejsce
def test_warhouse(capacity,result,products):
    w=Warehouse(capacity)        #two
    last_result=None
    for product in products:
        last_result=w.add(product)
    assert round(last_result,2) ==result #zaokreglenie do 2miejsc po przecinku
