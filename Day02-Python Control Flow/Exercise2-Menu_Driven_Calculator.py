def add(a, b):
    return(a + b)

def sub(a, b):
    return(a - b)

def multi(a, b):
    return(a * b)

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "division is not possible"

while True:
    print("\n Menu")
    print("1. Addition:")
    print("2. Subtraction:")
    print("3. Multiplication:")
    print("4. Divide:")
    print("5. Exit")

    choice = input("Enter your number: ")

    if choice == "5":
        print("Exiting Program.")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number:"))

    if choice == "1":
        print("Results: ", add(num1, num2))
    elif choice == "2":
        print("Results: ", sub(num1, num2))
    elif choice == "3":
        print("Results: ", multi(num1, num2))
    elif choice == "4":
        print("Results: ", div(num1, num2))
    else:
        print("Invalid Input")
