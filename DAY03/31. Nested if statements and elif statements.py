# Nested if statements and elif statements
#
#
# If you have to make options more than two in one condition.
#
# e.g.
# 
# if condition:               # 1st condition true
#     if another condition:   # 1st condition true 2nd condition true
#         do this 
#     else:                   # 1st condition true 2nd condition false
#         do this
# else:
#     do this
# 
# e.g.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age <= 18:
        print("please pay $7.")
    else:
        print("please pay $12.")
else:
        print("Sorry, you have to grow taller before you can ride.")

# Then, The way to make one more option in 2nd condition.
# We can use 'elif'
# e.g
# if condition1:
#   do A
# elif condition2:
#   do B
# else:
#   do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster!") 
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("please pay $7.")
    else:
        print("please pay $12.")
else:
        print("Sorry, you have to grow taller before you can ride.")