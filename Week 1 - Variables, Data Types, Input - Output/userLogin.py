username = input("Please enter your username = ")
userAge = input("Please enter your age = ")
userCity = input("Please enter your city = ") # Here we get the necessary information from the user

with open("user_data.txt", "w", encoding="utf-8") as file: # Here we ensure that the given information is written
    # to a different file
    file.write(f"Username = {username}\n")
    file.write(f"Age = {userAge}\n")
    file.write(f"City = {userCity}\n") # here we write the information we want to be recorded

print("We have successfully saved the information you entered.")