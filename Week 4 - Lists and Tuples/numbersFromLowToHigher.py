def sort_list(lst): # I define a function named sort_list that takes a list to be sorted
    n = len(lst) # counts how many numbers are in the list and saves it to the variable named n
    for i in range(n): # The outer main loop will scan the entire list from start to finish as many times as the number of elements in the list
        for j in range(0, n - i - 1): # The inner loop compares adjacent numbers and moves the larger one towards the end of the list
            if lst[j] > lst[j + 1]: # If the number on the left is greater than the one on the right, meaning they are in the wrong order
                temp = lst[j] # backs up the larger number on the left so it doesn't get lost
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
    return lst # stops the process and returns the sorted list when everything is finished

user_list = [] # Empty list to store the numbers we will get from the user
counter = 0

while counter < 5:
    number = int(input("Please enter the 5 numbers you want to list = "))
    user_list.append(number)
    counter += 1

sorted_list = sort_list(user_list)
print(sorted_list)