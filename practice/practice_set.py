
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)

union_set = set_a | set_b
print("Union (A | B):", union_set)

intersection_set = set_a & set_b
print("Intersection (A & B):", intersection_set)

difference_set = set_a - set_b
print("Difference (A - B):", difference_set)

symmetric_diff_set = set_a ^ set_b
print("Symmetric Difference (A ^ B):", symmetric_diff_set)

set_a.add(10)
print("Set A after adding 10:", set_a)

set_a.discard(3)
print("Set A after discarding 3:", set_a)

print("Is 4 in Set A?", 4 in set_a)

print("Elements in Set B:")
for item in set_b:
    print(item)
