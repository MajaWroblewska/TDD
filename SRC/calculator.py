import pytest

def add_numbers(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a+b
    else:
        raise Exception('Argument musi być liczbą')
# def pow_number(a):
#     return a**2



