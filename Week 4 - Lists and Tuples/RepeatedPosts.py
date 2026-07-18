def remove_duplicates(lst):
    new_list = []

    for number in lst:
        if number not in new_list:
            new_list.append(number)
    return new_list

original_list = [2,2,2,2,2,2]
clean_list = remove_duplicates(original_list)
print(clean_list)