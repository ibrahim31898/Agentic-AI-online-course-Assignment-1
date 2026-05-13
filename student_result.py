# Student Result System:

# Taking student information
student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

# Taking marks input (type casting to float)
marks1 = float(input("Enter Marks of Subject 1: "))
marks2 = float(input("Enter Marks of Subject 2: "))
marks3 = float(input("Enter Marks of Subject 3: "))

# Calculating total and percentage
total_marks = marks1 + marks2 + marks3
percentage = (total_marks / 300) * 100 

# Determining grade and result
if percentage >= 80:
    grade = "A+"
    result = "Pass"
elif percentage >= 70:
    grade = "A"
    result = "Pass"
elif percentage >= 60:
    grade = "B"
    result = "Pass"
elif percentage >= 50:
    grade = "C"
    result = "Pass"
else:
    grade = "Fail"
    result = "Fail"

# Displaying output
print("\n--- Student Result ---")
print(f"Student Name: {student_name}")
print(f"Roll Number: {roll_number}")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Result: {result}")
print(f"Grade: {grade}")