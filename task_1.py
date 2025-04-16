# Task 1: Create a Dictionary of Student Marks

# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

# result = {'ram':56, 'shyam':70, 'mohan': 33, 'radhe':89}
# name = input("Enter the Student's name:")
# if name in result.keys():
    
#     print(f"{name}'s marks:", result[name])
# else:
#     print("Student not found.")

result = {}
n = int(input("Enter the total number of students:"))

for i in range(n):
    key = input("enter student name:")
    value = input("enter marks of student:")
    result[key] = value
    
name = input("Enter the Student's name whose marks you want to know:")
if name in result.keys():
    
    print(f"{name}'s marks:", result[name])
else:
    print("Student not found.")