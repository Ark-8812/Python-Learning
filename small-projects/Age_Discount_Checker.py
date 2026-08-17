age = int(input("What is your age? "))  # input for the user's age

if age <= 18:
    print("Discount not applied")
else:
    print("Discount Applied")

checkout = input("Proceed to checkout? ")

if checkout == "yes" or checkout == "Yes":
    print("Thank you for shopping with us!")
else:
    print("OK! Please come back later")

print("Have a good day!")