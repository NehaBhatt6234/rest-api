
num_students = int(input("Enter the number of students: "))

students = []

for i in range(num_students):
    print(f"\nEnter data for Student {i+1}")
    name = input("Name: ")

    marks = []
    subjects = ["Math", "Science", "English", "History", "Computer"]

    for subject in subjects:
        score = float(input(f"Enter marks in {subject} (out of 100): "))
        marks.append(score)

    total = sum(marks)
    average = total / len(subjects)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    student_data = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student_data)

print("\n" + "="*50)
print("STUDENT REPORT")
print("="*50)

for student in students:
    print(f"Name: {student['name']}")
    print(f"Marks: {student['marks']}")
    print(f"Total: {student['total']:.2f}")
    print(f"Average: {student['average']:.2f}")
    print(f"Grade: {student['grade']}")
    print("-" * 50)
