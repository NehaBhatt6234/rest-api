
my_tuple = ("apple", "banana", "cherry", "apple", 42)

print("Original tuple:", my_tuple)

print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

print("Sliced tuple (1:3):", my_tuple[1:3])

print("Length:", len(my_tuple))

print("Count of 'apple':", my_tuple.count("apple"))

print("Index of 'cherry':", my_tuple.index("cherry"))

try:
    my_tuple[1] = "orange"
except TypeError as e:
    print("Error:", e)
