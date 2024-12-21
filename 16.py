option = input("Enter your menu choice (Pizza, Burger, Pasta): ")
if option.lower() == "pizza":
    print("$10")
elif option.lower() == "burger":
    print("$7")
elif option.lower() == "pasta":
    print("$8")
else:
    print("Invalid menu option.")