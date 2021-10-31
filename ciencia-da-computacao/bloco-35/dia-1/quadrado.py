class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return self.lado * 4


# Para testar!
quadrado_1 = Quadrado(5)
print(quadrado_1.calcular_area())  # 25
print(quadrado_1.calcular_perimetro())  # 20
assert quadrado_1.calcular_area() == 25
assert quadrado_1.calcular_perimetro() == 20
