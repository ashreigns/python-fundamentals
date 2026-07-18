examGrade = int(input("Please enter your exam grade = "))

if examGrade < 50:
    print("Your exam grade result = FF")
elif examGrade < 55:
    print("Your exam grade result = DD")
elif examGrade < 60:
    print("Your exam grade result = DC")
elif examGrade < 70:
    print("Your exam grade result = CC")
elif examGrade < 80:
    print("Your exam grade result = CB")
elif examGrade < 85:
    print("Your exam grade result = BB")
elif examGrade < 90:
    print("Your exam grade result = BA")
elif examGrade <= 100:
    print("Your exam grade result = AA")
else:
    print("Your grade is invalid, please enter a grade between 0-100.")


# Week 2 start: usage of if, elif, and else