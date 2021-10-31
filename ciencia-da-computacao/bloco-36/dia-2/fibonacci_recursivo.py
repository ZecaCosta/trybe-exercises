def fibonacci(n):
    if n < 2:
        print(f"o valor IF de n é {n}")
        return n
    else:
        print(f"o valor ELSE de n é {n}")
        hum = fibonacci(n-1)
        print(f"o valor de hum é {hum}")
        dois = fibonacci(n-2)
        print(f"o valor de dois é {dois}")
        return hum + dois


print(f"fibonacci(0) = {fibonacci(0)}")
print(f"fibonacci(1) = {fibonacci(1)}")
print(f"fibonacci(2) = {fibonacci(2)}")
print(f"fibonacci(3) = {fibonacci(3)}")
print(f"fibonacci(4) = {fibonacci(4)}")
print(f"fibonacci(5) = {fibonacci(5)}")
