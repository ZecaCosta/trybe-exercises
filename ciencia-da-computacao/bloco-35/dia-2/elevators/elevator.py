# ABSTRAÇÃO
# ENCAPSULAMENTO
# Interface
from abc import ABC, abstractmethod


class Ordenador:
    def chamar(self, chamados, andar):
        chamados.append(andar)
        return chamados


class ElevadorBase(ABC):
    def __init__(self, andar_inicial=0, ordenador=Ordenador()):
        """Construtor do elevador"""
        self._andar = andar_inicial
        self._chamados = []
        self._ordenador = ordenador

    @abstractmethod
    def ir(self):
        """Move o elevador."""
        pass

    def chamar(self, andar):
        """Adiciona o andar chamado na lista de chamados."""
        self._chamados = self._ordenador.chamar(andar)

    def localizar(self):
        """Indica o andar em que o elevador está."""
        return self._andar


class Elevador(ElevadorBase):
    def ir(self):
        """Vai para o próximo andar na lista de chamados."""
        if self._chamados:
            self._andar = self._chamados[0]
            self._chamados = self._chamados[1:]
