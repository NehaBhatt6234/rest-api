
fruits = ["apple", "banana", "cherry", "orange"]
print("Original list:", fruits)

fruits.append("mango")
print("After adding mango:", fruits)

fruits.remove("banana")
print("After removing banana:", fruits)

print("First fruit:", fruits[0])

print("All fruits:")
for fruit in fruits:
    print(fruit)

fruits.sort()
print("Sorted list:", fruits)

print("Number of fruits:", len(fruits))
