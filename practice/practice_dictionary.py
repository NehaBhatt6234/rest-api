
student = {
    "name": "Alice",
    "age": 21,
    "course": "Computer Science",
    "grades": [85, 90, 92]
}

print("Student Dictionary:", student)

print("Name:", student["name"])
print("Grades:", student["grades"])

student["email"] = "alice@example.com"
print("After adding email:", student)

student["age"] = 22
print("After updating age:", student)

del student["course"]
print("After deleting course:", student)

print("\nStudent Details:")
for key, value in student.items():
    print(f"{key}: {value}")

if "name" in student:
    print("\nName is present in the dictionary.")

print("Phone:", student.get("phone", "Not available"))
