# There are different data types in Python.
# You can check what type something is by using the type() function.

print(type("Hello"))   # This is a string (text)
print(type(13))        # This is an integer (whole number)
print(type(3.14))      # This is a float (decimal number)

# When you use input(), Python ALWAYS gives you a string, even if you type a number.
age = input("How old are you? ")
print("Before converting, age is:", age)
print("The type of age is:", type(age))

# You can convert a string into an integer using int().
age = int(age)
print("After converting, age is:", age)
print("The type of age is now:", type(age))

# Now you can do maths with it.
print("Next year you will be", age + 1)

# You can also convert numbers into strings using str().
year = 2026
year_text = str(year)
print("The year as text is:", year_text)
print("The type of year_text is:", type(year_text))

# You can convert a string into a float using float().
height = input("What is your height in metres? ")
print("Before converting, height is:", height)
print("The type of height is:", type(height))

height = float(height)   # Convert to a float (decimal number)
print("After converting, height is:", height)
print("The type of height is now:", type(height))

# You can do maths with floats too.
print("Double your height is:", height * 2)
