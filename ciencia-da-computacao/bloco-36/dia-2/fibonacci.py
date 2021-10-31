def fibonacci_iter(n):
    sequence = [0, 1]
    if n >= 2:
        for x in range(2, n+1):
            print(f"o valor de x é {x}")
            print(type(range(2, n+1)))
            print((range(2, n+1)))
            next = sequence[-1] + sequence[-2]
            print(f"o valor de sequence[-1] é {sequence[-1]}")
            print(f"o valor de sequence[-2] é {sequence[-2]}")
            print(f"o valor de next é {next}")
            sequence.append(next)
            print(sequence)
    return sequence[n]


print(fibonacci_iter(0))
print(fibonacci_iter(1))
print(fibonacci_iter(2))
print(fibonacci_iter(3))
print(fibonacci_iter(4))
