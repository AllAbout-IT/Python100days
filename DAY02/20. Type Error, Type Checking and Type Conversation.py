#  Type Error, Type Checking and Type Conversation

# num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters.")
#   - TypeError: can only concatenate str (not "int") to str

# print(type(num_char))

###############################################################

# num_char = len(input("What is your name?"))

# new_num_char =str(num_char) # If you want to appeared number of function, put it inside parentheses of a str function.

# print("Your name has " + new_num_char + " characters.")

a = 123
print(type(a))
#       - ype(object) -> the object's type type(name, bases, dict, **kwds) -> a new type

b = str(123)
print(type(b))

print(70+float("100.5"))
#   It means 70+100.5. So, the Answer is 170.5

# So, What would print here?
print(str(70)+str(100))
# You know, It would process in the strings. It would be '70100'
