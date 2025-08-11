# Number Classifier Program

# Get input from the user
number = float(input("Enter any number: "))

if number > 0:
    print("The number is positive.")

    if number > 1000:
        print("It's a large positive number.")
    elif number > 100:
        print("It's a moderately large number.")
    else:
        print("It's a small positive number.")

elif number < 0:
    print("The number is negative.")

    if number < -1000:
        print("It's a large negative number.")
    elif number < -100:
        print("It's a moderately large negative number.")
    else:
        print("It's a small negative number.")

else:
    print("The number is zero.")
