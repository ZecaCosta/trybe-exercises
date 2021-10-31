class Gerenciador:
    def __init__(self, elevadores):
        self.elevadores = elevadores

    def localizar(self):
        return [elevador.localizar() for elevador in self.elevadores]
