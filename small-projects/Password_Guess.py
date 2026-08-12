#This is my password guess project
password = "hello world" 
guess = input() #This will ask the user for the first guess
while guess != password: #This while loop will run until the correct password is entered 
    print("Password is incorrect please  try again")
    guess = input() #If the password is incorrect then it will ask for user input again 

print("Password is correct") #If the user password is correct then it will say that the password is correct 