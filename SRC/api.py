
class API:
    @classmethod
    def get_data(cls):
        return "03570,88,99ugu,ui0,p5p"

    def __init__(self):
        self.zmienna = 5

def get_only_numbers():
    numbers = []
    for line in API.get_data():
        digits = [x.strip() for x in line.split(',') if x.strip().isdigit()]
        numbers.extend(digits)

    return '|'.join(numbers)

print(get_only_numbers())


class API2:
    @classmethod #metoda działa bez tworzenia obiektu na klasie nie moe być zmiennych obiektu i metod obiektu
    def get_data(cls):
        return open('aa').readlines()
    def get_only_numbers():
        numbers=[]
        for line in API2.get_data():
            digit=[x.strip() for x in line.split(",") if x.strip().isdigit()]
            numbers.extend(digit)
        return '|'.join(numbers)

print(get_only_numbers())