def checkvc(char):
    vowels = 'aeiouAEIOU'
    if char in vowels:
        return f"{char} is a vowel."
    else:
        return f"{char} is a consonant."
char = input("Enter a character: ")
if len(char) == 1 and char.isalpha():
    result = checkvc(char)
    print(result)
else:
    print("Please enter a single alphabetic character.")
