marks = int(input("Enter your marks: "))
if 90 <= marks <= 100:
    grade = 'A'
elif 80 <= marks <= 89:
    grade = 'B'
elif 70 <= marks <= 79:
    grade = 'C'
else:
    grade = 'Fail'
print(f"Your grade is: {grade}")
