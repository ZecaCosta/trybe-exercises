from abc import ABC, abstractmethod
import json


class SalesReport(ABC):
    def __init__(self, export_file):
        self.export_file = export_file

    def build(self):
        return [{
                'Coluna 1': 'Dado 1',
                'Coluna 2': 'Dado 2',
                'Coluna 3': 'Dado 3'
                },
                {
                'Coluna 1': 'Dado A',
                'Coluna 2': 'Dado B',
                'Coluna 3': 'Dado C'
                }]

    @abstractmethod
    def serialize(self):
        raise NotImplementedError

    @abstractmethod
    def get_length(self):
        raise NotImplementedError


class SalesReportJSON(SalesReport):
    def serialize(self):
        with open(self.export_file + '.json', 'w') as file:
            json.dump(self.build(), file)

    def get_length(self):
        return 4


# Para testar

# TypeError: Can't instantiate abstract class SalesReportJSON
# with abstract methods get_length
meu_relatorio_de_vendas = SalesReportJSON('meu_relatorio')
print(meu_relatorio_de_vendas.get_length())


# TypeError: Can't instantiate abstract class SalesReport
# with abstract methods serialize
relatorio_de_vendas = SalesReport('relatorio_de_vendas')
