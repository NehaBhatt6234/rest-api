# 1. Define simple functions
def greet(name):
    return f"Hello, {name}!"

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

# 2. Assign function to a variable
say_hello = greet
print(say_hello("Alice"))  # Output: Hello, Alice!

# 3. Pass function as argument
def greet_with_style(func):
    return func("Hello World")

print(greet_with_style(shout))   # Output: HELLO WORLD
print(greet_with_style(whisper)) # Output: hello world

# 4. Return function from another function
def get_greeting_function(style='formal'):
    def formal(name):
        return f"Good day, {name}."

    def casual(name):
        return f"Hey {name}!"

    if style == 'formal':
        return formal
    else:
        return casual

formal_greet = get_greeting_function('formal')
casual_greet = get_greeting_function('casual')

print(formal_greet("John"))  # Output: Good day, John.
print(casual_greet("John"))  # Output: Hey John!

# 5. Store functions in a data structure (dictionary)
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply
}

print(operations["add"](10, 5))       # Output: 15
print(operations["subtract"](10, 5))  # Output: 5
print(operations["multiply"](10, 5))  # Output: 50
