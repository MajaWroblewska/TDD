# @classmethod #metoda działa bez tworzenia obiektu na klasie nie moe być zmiennych obiektu i metod obiektu
# >>> metoda działa bez tworzenia obiektu na klasie nie moze być zmiennych obiektu i metod obiektu
# @classmethod stoi przy innej metodzie nie przy __init__

#klasa 2 z @classmethod
class API2:
    def __init__(self):
        self.napis='tekst135'          #=input('Pisz:')

    @classmethod
    def get_data(self):
        return 'wazny napis963'     #=input('Pisz:')   #to ważne

#działa
def get_only_number():
    liczba=([znak for znak in API2.get_data() if znak.isdigit()])   # nie musi być obiekt klasy bo jest @classmethod w klasie
                                                                    # odwołanie przez Klase.metoda =API2.get_data()
    print(liczba) #>>>['9','6','3']
    return ('|'.join(liczba))

print(get_only_number())

########################################################################################################################
#klasa 1
class API:
    def __init__(self):
        self.napis='tekst135'          #=input('Pisz:')
    def get_data(self):
        return self.napis

api=API()
# print(api.napis)        #>>> tekst135
# print(api.get_data())   #>>> tekst135

#działa
def get_only_number():
    liczba=([znak for znak in api.get_data() if znak.isdigit()])  #comprachentoion list/
                                                                  #odwołanie do wcześniej stworzonego obiektu api=API()
                                                                  # mam dostęp do danych z inita bo stworzony obiekt api-API() wiec
                    # metoda get_data ma dostęp do inita self.napis='tekst135'
    print(liczba) #>>>['1','3','5']
    return ('|'.join(liczba))

print(get_only_number())



