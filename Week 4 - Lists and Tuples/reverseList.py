def reverse_list(lst):
    reversed_list = []

    for element in lst:
        reversed_list.insert(0, element)
    return reversed_list

original_list = [10, 20, 30, 40, 50]
result = reverse_list(original_list)
print(result)