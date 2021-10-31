def multiply_arrays(array1, array2, array3):
    result = []
    number_of_iterations = 0

    for number1 in array1:
        print(f'Array 1: {number1}')
        for number2 in array2:
            print(f'Array 2: {number2}')
            for number3 in array3:
                print(f'Array 3: {number3}')
                result.append(number1 * number2 * number3)
                number_of_iterations += 1

    print(f'{number_of_iterations} iterações!')
    return result


meu_array = list(range(1, 201))

# meu_array = list(range(1, 101))
# 1.000.000 iterações
# real    0m14,129s
# user    0m4,624s
# sys     0m3,256s

# meu_array = list(range(1, 201))
# 8.000.000 iterações
# real    1m54,136s
# user    0m38,000s
# sys     0m26,232s


multiply_arrays(meu_array, meu_array, meu_array)

# para rodar no terminal e verificar o tempo de execução
# time python3 cubico.py
