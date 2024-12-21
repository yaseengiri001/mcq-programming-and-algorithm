c= input("Enter a character: ")
if c.isupper():
    print(f"The character is uppercase")
elif c.islower():
    print(f"The character is lowercase")
elif c.isdigit():
    print(f"The character is a digit")
else:
    print(f"The character is not a letter or digit")