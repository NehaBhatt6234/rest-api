

while True:
    print("\n===== MENU =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '4':
        print("Exiting program. Goodbye!")
        break  # exits the loop

    # Take two numbers as input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    else:
        print("Invalid choice. Please enter 1-4.")
