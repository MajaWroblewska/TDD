# klasa 2 z @classmethod
# >>> metoda działa bez tworzenia obiektu na klasie nie moze być zmiennych obiektu i metod obiektu
# @classmethod przy metodzie nie przy __init__
class API:
    def __init__(self):
        self.napis='tekst135'          #=input('Pisz:')

    # ["1,4,5,25,aa,bb,23,4", "324,24,234www,1,23", "545,3w,32"]#
    @classmethod
    def get_data(self):
        return "1,4,5,25,aa,bb,23,4"     #=input('Pisz:')   #to ważne
#działa
def get_only_numbers():
    numery=[]
    for line in API.get_data():
        liczba=[znak.strip() for znak in line.strip(',') if znak.strip().isdigit()]# znak.strip() usówa białe znaki z przodu i z tyły strniga
                                                            # nie musi być obiekt klasy bo classmethod
                                                                    # odwołanie przez Klase.metoda =API2.get_data()
        numery.extend(liczba)
    # numbers.extend(digits)
    #   digits = [x.strip() for x in line.split(',') if x.strip().isdigit()]
    # print(liczba) #>>>['9','6','3']
    return ('|'.join(numery))

print(get_only_numbers())

########################################################################################################################
# #klasa 1
# class API:
#     def __init__(self):
#         self.napis='tekst135'          #=input('Pisz:')
#     def get_data(self):
#         return self.napis
#
# api=API()
# # print(api.napis)        #>>> tekst135
# # print(api.get_data())   #>>> tekst135
#
# #działa
# def get_only_number():
#     liczba=([znak for znak in api.get_data() if znak.isdigit()])  #comprachentoion list/
#                                                                   #odwołanie do wcześniej stworzonego obiektu api=API()
#                                                                   # mam dostęp do danych z inita bo stworzony obiekt api-API() wiec
#                                                                   # metoda get_data ma dostęp do inita self.napis='tekst135'
#     print(liczba) #>>>['1','3','5']
#     return ('|'.join(liczba))
#
# print(get_only_number())
