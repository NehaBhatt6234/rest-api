
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # calling parent constructor
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers")

print(dog.speak())    # Buddy says Woof!
print(cat.speak())    # Whiskers says Meow!
