def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Alice", 25)

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(age=30, name="Bob")

def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")

# Uses default age
greet("Charlie")

greet("Daisy", 22)

def add_numbers(*args):
    total = sum(args)
    print("Sum:", total)

add_numbers(1, 2)
add_numbers(5, 10, 15, 20)

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Eve", age=28, city="Paris")




