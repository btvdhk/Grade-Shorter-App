print("Welcome to the Grade Shorter App")

grades = []
grade = input("\nWhat is your first grade (0-100): ")
grades.append(grade)
grade = input("What is your second grade (0-100): ")
grades.append(grade)
grade = input("What is your third grade (0-100): ")
grades.append(grade)
grade = input("What is your fourth grade (0-100): ")
grades.append(grade)

print(f"\nYour grades are: {grades}")

grades.sort(reverse=True)
print(f"\nYour grades from highest to lowest are: {grades}")

print(f"\nThe lowest two grades will now dropped.")
remove = grades.pop()
print(f"\nRemoved grade: {remove}")
remove = grades.pop()
print(f"\nRemoved grade: {remove}")

print(f"\nYpur remaining grades are: {grades}")
print(f"Nice work! Your highest grade is: {grades[0]}.")
