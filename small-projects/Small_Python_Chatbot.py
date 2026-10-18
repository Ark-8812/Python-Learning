import random #Importing the nessasary modules
# Intro
print("Welcome to PythonBot!")
print("Type 'help' to see what I can do!")
print("Type 'bye' if you want to exit!")

name = input("What is your name: ")
print("Hello", name, "! Nice to meet you!!!")

# Main Loop
message = ""

while message != "bye": #This will run until the user decides to quit by saying "bye"
    print("") #Creating a blank line
    print("What would you like to do!!!") #Different Options for the user
    print("1. Calculator")
    print("2. Mood Check")
    print("3. Joke")
    print("4. Random Number Game")
    print("5. Name Initials")
    print("Type 'help' to see the options.")
    print("Type 'bye' to exit.")

    message = input("\nYou: ").lower() #This will make what ever the user types in lowercase

    # Asking what the user wants
    if message == "help":
        print("Choose option 1, 2, 3, 4 or 5.")

    elif message == "1":
        print("You have chosen the calculator!") #Calculator
        num1 = int(input("What do you want your first number to be: "))
        num2 = int(input("What do you want your second number to be: "))
        calculation = input("What operation would you like to do (enter *, /, - or +): ")

        if calculation == "+": #Condtions for the calculator
            print(num1 + num2)
        elif calculation == "-":
            print(num1 - num2)
        elif calculation == "/":
            if num2 != 0:
                print(num1 / num2)
            else:
                print("You cannot divide by zero!")
        elif calculation == "*":
            print(num1 * num2)
        else:
            print("Invalid operation. Please enter +, -, / or *.")

    elif message == "2":
        print("You have chosen Mood Check!")
        feeling = input("How are you feeling today (sad🥺, happy😁, tired😴)").lower()
        if feeling == "sad":
          print("Aw, if something is bothering you a lot, you should go and speak to an trusted adult")
        elif feeling == "happy":
          print("THATS GREAT!!! Hope your day stays happy!!")
        elif feeling == "tired":
          print("Dam! You should get some sleep or some rest if you can!")
        else:
          print("Sorry this is not a valid option: Pick from sad, happy, tired!!")

    elif message == "3":
        print("You have chosen a Joke!")
        print("Here's some funny jokes!")
        print("Why don't eggs tell jokes? They might crack up!")
        print("Stop looking for the perfect match; use a lighter.")
        print("How do you stop a bull from charging? Cancel its credit card.")
        print("What did one wall say to the other wall? I'll meet you at the corner!")
        print("I was going to tell you a joke about time travel, but you didn't like it.")
        print("I'm writing a book about glue, but I'm stuck on the first chapter.")

    elif message == "4":
        print("You have chosen the Random Number Game!")
        secret = random.randint(1, 10) #Generate a random number between 1-10
        guess = 0
        attemps = 0
        while guess != secret:
          guess = int(input("Please enter a number: "))
          attemps = attemps + 1 #Every guess will add to the attemps
          if guess > secret:
            print("Too High! Try again")
          elif guess < secret:
            print("Too low! Try again")
          else:
            print("You guessed it!!! Well done!")
            print("Attemps: ", attemps)

    elif message == "5":
        print("You have chosen Name Initials!")
        last_name = input("What is your second name?")
        initials = name[0].upper() + last_name[0].upper() #0 tells us what letter we want. computer start counting from 0 so the first letter would be 0
        print(initials)                                    #.Upper() makes the letters uppercase
    elif message == "bye":
        print("Goodbye", name, "!")

    else:
        print("Invalid input. Please type 'help' to see the options.")

    if message != "bye":
        print("What would you like to do now?")
