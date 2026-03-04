print("Simple Calculator")

#Creating 2 inputs for the user 
num1 = float(input("What is your first number: "))  
num2 = float(input("What is your second number: "))

print("Choose a operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice (1-4)"))

if choice == 1:
    print("Result:", num1 + num2)
elif choice == 2:
    print("Result:", num1 - num2)
elif choice == 3:
    print("Result:", num1 * num2)
elif choice == 4:
    print("Result:", num1 / num2)
else:
    print("Invalid choice")
