#w funkcji:
# gdy return to wywołanie musimy printem -print(wywołanie)
# gdy print to wywolanie bez print - wywołanie()

#działa
def get_only_number1():
    string='la356lal32 '    #input('podaj napis z cyframi:')
    liczba=([znak for znak in string if znak.isdigit()]) #
    print(liczba) #>>>['3','5','6','3','2']
    return ('|'.join(liczba)) #>>> 3|5|6|3|2

print(get_only_number1())
print('*'*30)

#działa
def get_only_number2():
    string='la356lal32 ' #=input('Wpisz coś:)
    liczba=([znak for znak in string if znak.isdigit()])
    # print(liczba) #>>>['3','5','6','3','2']
    print('|'.join(liczba)) #>>> 3|5|6|3|2

get_only_number2()
print('*'*30)

#działa
def get_only_number():
    string='la1 23 l4ala5 '       #input('podaj napis z cyframi:')
    cyfry=[]
    litery=[]
    for znak in string:
        if znak.isdigit():
            cyfry.extend(znak)
        elif znak.isalpha():
            litery.extend(znak)
    return  '|'.join(cyfry) , '|'.join(litery)


print(get_only_number())