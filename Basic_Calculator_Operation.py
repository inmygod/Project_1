# First User Screen
print("Calculator")
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")

# Input from Options
option = int(input("Select an Option for Basic Calculator Operation: "))

# Option 1: Addition
if option == 1:
    n1 = int(input("Enter 1st Number"))
    n2 = int(input("Enter 2nd Number"))
    n3 = n1 + n2
    print(n3)
# Option 2: Subtraction
elif option == 2:
    n1 = int(input("Enter 1st Number"))
    n2 = int(input("Enter 2nd Number"))
    n3 = n1 - n2
    print(n3)
# Option 3: Multiplication
elif option == 3:
    n1 = int(input("Enter 1st Number"))
    n2 = int(input("Enter 2nd Number"))
    n3 = n1 * n2
    print(n3)
# Option 4: Division
elif option == 4:
    n1 = int(input("Enter 1st Number"))
    n2 = int(input("Enter 2nd Number"))
    n3 = n1 / n2
    print(n3)
else:
    print("Invalid Input")