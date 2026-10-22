def grade_for(marks):
	if marks >= 90:
		return "A"
	if marks >= 80:
		return "B"
	if marks >= 70:
		return "C"
	if marks >= 60:
		return "D"
	return "F"


students = []

print("Enter the name and marks for five students.")
for student_number in range(1, 6):
	name = input(f"Student {student_number} name: ").strip()

	while True:
		try:
			marks = float(input(f"{name}'s marks (0-100): "))
		except ValueError:
			print("Please enter a number.")
			continue

		if 0 <= marks <= 100:
			break
		print("Marks must be between 0 and 100.")

	students.append((name, marks, grade_for(marks)))

print("\nGrade boundaries: A = 90-100, B = 80-<90, C = 70-<80, D = 60-<70, F = <60")
print("\n{:<5} {:<20} {:>8} {:>8}".format("No.", "Name", "Marks", "Grade"))
print("-" * 45)
for student_number, (name, marks, grade) in enumerate(students, start=1):
	print("{:<5} {:<20} {:>8.2f} {:>8}".format(student_number, name, marks, grade))
