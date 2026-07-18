def query_grade(name):
    # Our dictionary (database) that stores student names and their grades
    student_record = {
        "ahmet": 85,
        "ayşe": 95,
        "mehmet": 70,
        "fatma": 100,
        "can": 55
    }
    # We convert the searched name to lowercase to prevent capitalization errors
    searched_name = name.lower()
    # if name in dict logic: Does the name exist among the dictionary keys?
    if searched_name in student_record:
        # We retrieve the grade value associated with that name from the dictionary
        student_grade = student_record[searched_name]
        return student_grade
    else:
        return None

user_input = input("Enter the name of the student whose grade you want to learn = ")

grade_result = query_grade(user_input)

if grade_result is not None:
    print(f"The grade of the student named {user_input.capitalize()} = {grade_result}")
else:
    print("No such student is registered in the system.")