# 1. Basic Decorator
def simple_decorator(func):
    def wrapper():
        print("[Simple] Before the function runs")
        func()
        print("[Simple] After the function runs")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

# 2. Decorator with function arguments
def greet_decorator(func):
    def wrapper(name):
        print("[Greet] Preparing to greet...")
        func(name)
        print("[Greet] Greeting complete!")
    return wrapper

@greet_decorator
def greet(name):
    print(f"Hello, {name}!")

# 3. Universal Decorator with *args and **kwargs
def universal_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[Universal] Calling '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[Universal] '{func.__name__}' returned: {result}")
        return result
    return wrapper

@universal_decorator
def add(x, y):
    return x + y

@universal_decorator
def multiply(x, y):
    return x * y

# 4. Chaining multiple decorators
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclaim_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

@exclaim_decorator
@uppercase_decorator
def say_message():
    return "hello world"

# === RUNNING ALL FUNCTIONS ===
print("---- 1. Basic Decorator ----")
say_hello()

print("\n---- 2. Decorator with Arguments ----")
greet("Alice")

print("\n---- 3. Universal Decorator ----")
add(5, 3)
multiply(4, 7)

print("\n---- 4. Chained Decorators ----")
print(say_message())
