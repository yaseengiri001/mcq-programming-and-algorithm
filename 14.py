def x(age, experience):
    if age > 18 and experience >= 2:
        return "Eligible"
    else:
        return "Not Eligible"
age = int(input("Enter age: "))
experience = int(input("Enter years of experience: "))
print(x(age, experience))