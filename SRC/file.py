def get_data(how_much):
    with open("dane.txt",'r') as f:
        return f.read(how_much)

def get_avg(how_much):
    data=get_data(how_much)         #przypisnie w zmiennej data do
    numbers=[int(x) for x in data]          #comprahension list jako lista zamiana str na int ze zczytanego pliku.txt
    return sum(numbers)/len(numbers)        #średnia


# print(get_data(3))
# print(get_avg(3))