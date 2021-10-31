class Televisão:
    def __init__(self, tamanho):
        self.volume = 20
        self.canal = 539
        self.taxa_volume = 2
        self.tamanho = tamanho
        self.ligada = False

    def aumentar_volume(self):
        self.volume += self.taxa_volume

    def diminuir_volume(self):
        self.volume -= self.taxa_volume

    def modificar_canal(self, novo_canal):
        self.canal = novo_canal

    def ligar_ou_desligar(self):
        self.ligada = not self.ligada


tv_sala = Televisão(32)
print(tv_sala.tamanho)  # 32

print(tv_sala.volume)  # 20
tv_sala.aumentar_volume()
print(tv_sala.volume)  # 22

print(tv_sala.volume)  # 22
tv_sala.diminuir_volume()
print(tv_sala.volume)  # 20

print(tv_sala.canal)  # 539
tv_sala.modificar_canal(570)
print(tv_sala.canal)  # 570

print(tv_sala.ligada)  # False
tv_sala.ligar_ou_desligar()
print(tv_sala.ligada)  # True
