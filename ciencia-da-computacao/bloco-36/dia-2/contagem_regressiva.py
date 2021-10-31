lista = []


def contagem_regressiva(n):
    if n == 0:
        lista.append("Decolar")

    else:
        lista.append(n)
        contagem_regressiva(n - 1)

    return lista


print(contagem_regressiva(5))
