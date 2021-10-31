class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return self.base * 2 + self.altura * 2


# Para testar!
retangulo_1 = Retangulo(5, 4)
print(retangulo_1.calcular_area())  # 20
print(retangulo_1.calcular_perimetro())  # 18
assert retangulo_1.calcular_area() == 20
assert retangulo_1.calcular_perimetro() == 18
