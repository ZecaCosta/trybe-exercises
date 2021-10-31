def reverse(list):
    print(list)
    if len(list) < 2:
        return list
    else:
        # print(f'lista {list[1:]}')
        # print(list[0])
        return reverse(list[1:]) + [list[0]]
        # return reverse(list[1:]) + [list[0]]
        # return list[1:] + [list[0]]
        # return list[1:]


array = [1, 2, 3]
print(reverse(array))
