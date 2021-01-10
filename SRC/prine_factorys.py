
def prime_factors(x):
    lista=[]
    faktors = 2
    while x>1:
        while x % faktors == 0:
            lista.append(faktors)
            x= x / faktors
        faktors +=1
    return lista

print(prime_factors(48))


# def prime_factors(x):
#     primes = [2, 3, 5, 7, 11, 13, 17, 19]
#     li = list()
#     for prime in primes:
#         while x % prime == 0:
#             li.append(prime)
#             x = x / prime
#     return li