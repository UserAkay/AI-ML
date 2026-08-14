def student_grade():
    data1 = input("Enter your name: ")
    data2 = int(input("Enter your age: "))
    data3 = input("Enter your roll: ")

    data4 = float(input("Enter your Science grades: "))
    data5 = float(input("Enter your Maths grades: "))
    data6 = float(input("Enter your Physics grades: "))
    data7 = float(input("Enter your Chemistry grades: "))
    data8 = float(input("Enter your Hindi grades: "))

    # Store student data and grades in dictionaries
    student = {
        "name": data1,
        "age": data2,
        "roll": data3
    }

    grade = {
        "Science": data4,
        "Maths": data5,
        "Physics": data6,
        "Chemistry": data7,
        "Hindi": data8
    }

    print(student)
    print(grade)

    # Calculate the average grade
    grades = [data4, data5, data6, data7, data8]
    if all(0 <= g < 101 for g in grades):
        avg_grade = sum(grades) / len(grades)
        print("Average Grade:", avg_grade)
    else:
        print("Please enter Valid Grade")


# Call the function
student_grade()
