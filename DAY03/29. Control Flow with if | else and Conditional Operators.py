# condition
# if/else
# Depending on a particular condition, we would do either A or B.

# In python
if condition: # if + Our condition for test
    do this   # if above condition is true, it should be executed.  
              # but, above condition is not true. 
else:         # then, it will skip to else block
    do this   # it should be executed. 


# for example
water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")

# exercise
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?")) # you can write height you want.

if height >= 120:                                  # If the height value that you wrote above is equal(=) or greater(>) than 120,
    print("You can ride the rollercoaster!")      # It will be execute.
                                                  # If the above value is less than 120,
else:                                             # the processing skips the 'if' block and moves to the 'else.'
    print("Sorry, you have to grow taller before you can ride.")    # and then, it will be execute.


#     note
#   Operator    Meaning
#       >       Greater than
#       <       Less than
#       >=      Greater than or equal to
#       <=      Less than or equal to
#       ==      equal to
#       !=      not equal to
#
#   in addition
#       =       Assignment
#