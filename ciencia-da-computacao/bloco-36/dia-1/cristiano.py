def mais_que_vinte_cinco_por_cento(array):
    len_array = len(array)
    vinte_cinco_porcento = len_array // 4
    setenta_cinco_porcento = len_array - vinte_cinco_porcento

    for index, elemento in enumerate(array[:setenta_cinco_porcento]):
        if elemento == array[index + vinte_cinco_porcento]:
            return elemento
    return -1


if __name__ == "__main__":
    test1 = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    test2 = [1, 1, 2, 3]
    test3 = [1, 1, 1, 1]

print(f"O elemento encontrado para teste1: {test1}")
print(f"{mais_que_vinte_cinco_por_cento(test1)}")
print(f"O elemento encontrado para teste1: {test2}")
print(f"{mais_que_vinte_cinco_por_cento(test2)}")
print(f"O elemento encontrado para teste1: {test3}")
print(f"{mais_que_vinte_cinco_por_cento(test3)}")
