def linear_search(numbers, n):
    for index, number in enumerate(numbers):
        if(number == n):
            return index

    return -1


print(linear_search([1, 2, 3, 4, 5], 6))  # -1
print(linear_search([1, 2, 3, 4, 5], 4))  # 3
print(linear_search([1, 2, 3, 4, 5], 1))  # 0
