class Circulo:
    PI = 3.14159

    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return self.raio * self.raio * self.PI

    def calcular_perimetro(self):
        return self.raio * 2 + self.PI


# Para testar!
circulo_1 = Circulo(5)
print(circulo_1.calcular_area())  # 78.53975
print(circulo_1.calcular_perimetro())  # 13.14159
assert round(circulo_1.calcular_area(), 2) == 78.54
assert round(circulo_1.calcular_perimetro(), 2) == 13.14
