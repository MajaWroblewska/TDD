from SRC.odd_index import odd_indexes


def odd_indexes_string1():
    assert  odd_indexes('string')== "tig"
def odd_indexes_string1():
    assert  odd_indexes('komputer')== "optr"
def odd_indexes_int():
    assert odd_indexes(12345)=='24'