def reverse(array):
    if len(array) <= 1:
        return array
    else:
        return reverse([:len(array) - 1])


array = [1, 2, 3]
print(reverse(array))
