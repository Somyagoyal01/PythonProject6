"""Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message."""
dictionary= {'Alice':50,'Trivia':49,'Ram':91,'Sita':92,'Honey':80}
student_name=input("Enter student's name=")
if student_name in dictionary:
    print(f"{student_name}'s marks: {dictionary[student_name]}")
else:
    print("Student name not found")

