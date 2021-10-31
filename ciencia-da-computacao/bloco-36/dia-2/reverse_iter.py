def reverse(list):
    reversed_list = []
    for item in list:
        reversed_list.insert(0, item)
    return reversed_list


array = [1, 2, 3]
print(reverse(array))

assert reverse(array) == [3, 2, 1]
