class SmartOrdenador():
    def chamar(self, chamados, andar):
        if not chamados:
            return super().chamar(andar)

        mais_perto = 0
        menor_distancia = abs(andar - chamados[0])

        for index, chamado in enumerate(chamados[1:]):
            if abs(chamado - andar) < menor_distancia:
                mais_perto = index
                menor_distancia = abs(chamado - andar)

        chamados.insert(mais_perto, andar)

        return chamados
