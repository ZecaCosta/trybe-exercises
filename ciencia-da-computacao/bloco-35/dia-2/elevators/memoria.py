from elevators.elevator import ElevadorBase, Ordenador


class MemoriaElevador(ElevadorBase):
    def __init__(self, andar_inicial=0, ordenador=Ordenador(), memoria=0):
        self.memoria = memoria
        super().__init__()

    def voltar(self):
        ...
