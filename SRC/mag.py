class Product:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class Warehouse:
    def __init__(self, capacity):
        self.capacity = capacity
        self.products = [] #list()

    def calculate_free_space(self):
        sum_of_products = 0
        for i in self.products:
            sum_of_products += i.volume  #volume dostep przez tworzrnie obiekt klasy Produkt
        return self.capacity - sum_of_products

    def add(self, product):
        rest_space = self.calculate_free_space()
        if rest_space >= product.volume:
            self.products.append(product)
            return rest_space - product.volume
        else:
            return -1

wh1 = Warehouse(150)
p1 = Product("car", 60)
p2 = Product("motorbike", 30)
print(wh1.add(p1))
print(wh1.add(p2))