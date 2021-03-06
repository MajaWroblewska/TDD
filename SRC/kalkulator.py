class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dodaj(self):
        if isinstance(self.a, int) and isinstance(self.b, int):  #zabezpieczenie przed srtingami
            return self.a + self.b
        else:
            raise Exception("Argument musi być liczbą!")

    def odejmij(self, zamien=False):
        if isinstance(self.a, int) and isinstance(self.b, int):
            if not zamien:
                return self.a - self.b
            else:
                return self.b - self.a
        else:
            raise Exception("Argument musi być liczbą!")

    def mnoz(self):
        if isinstance(self.a, int) and isinstance(self.b, int):
            return self.a * self.b
        else:
            raise Exception("Argument musi być liczbą!")

    def dziel(self, zamien=False):
        if isinstance(self.a, int) and isinstance(self.b, int):
            if not zamien:
                return self.a / self.b
            else:
                return self.b / self.a
        else:
            raise Exception("Argument musi być liczbą!")

klalkulator1=Kalkulator(1,3)
print(klalkulator1.odejmij(zamien=True))
print(klalkulator1.odejmij(zamien=False))
