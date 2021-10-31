def multiply_arrays(array1, array2):
    result = []
    number_of_iterations = 0

    for number1 in array1:
        print(f'Array 1: {number1}')
        for number2 in array2:
            print(f'Array 2: {number2}')
            result.append(number1 * number2)
            number_of_iterations += 1

    print(f'{number_of_iterations} iterações!')
    return result


meu_array = list(range(1, 2001))

# meu_array = list(range(1, 1001))
# 1.000.000 iterações
# real    0m13,197s
# user    0m4,731s
# sys     0m3,485s

# meu_array = list(range(1, 2001))
# 4.000.000 iterações
# real    0m58,936s
# user    0m18,414s
# sys     0m13,109s

multiply_arrays(meu_array, meu_array)

# para rodar no terminal e verificar o tempo de execução
# time python3 range.py
