print("--------Mini Calculator--------\n\n\n")

while True:
    num1 = float(input("Enter first number here: "))
    num2 = float(input("Enter second number here: "))
    print("Press 1 for Addition\nPress 2 for Subtraction\nPress 3 for Multiplication\nPress 4 for Division")
    choice = int(input("Enter your choice from 1-4: "))

    if choice == 1:
        result = num1 + num2
        print("The sum of the two numbers is:", result)
    elif choice == 2:
        result = num1 - num2
        print("The subtraction of the two numbers is:", result)
    elif choice == 3:
        result = num1 * num2
        print("The multiplication of the two numbers is:", result)
    elif choice == 4:
        if num2 != 0:
            result = num1 / num2
            print("The division of the two numbers is:", result)
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print("Invalid input")

    # Exit prompt
    exit_choice = int(input("Process is finished. To exit, press 0. To continue, press any other number: "))
    if exit_choice == 0:
        print("Calculator exited. Thank you!")
        break
