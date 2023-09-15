# https://app.codingrooms.com/management/assignments/364915/overview
#
# Instructions
# Write a program that works out whether if a given number is an odd or even number.

# Even numbers can be divided by 2 with no remainder.

# e.g. 86 is even because 86 ÷ 2 = 43

# 43 does not have any decimal places. Therefore the division is clean.

# e.g. 59 is odd because 59 ÷ 2 = 29.5

# 29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

# e.g.

# 6 ÷ 2 = 3 with no remainder.

# therefore: 6 % 2 = 0

# 5 ÷ 2 = 2 x 2 + 1, remainder is 1.

# therefore: 5 % 2 = 1

# 14 ÷ 4 = 3 x 4 + 2, remainder is 2.

# therefore: 14 % 4 = 2

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input 1
# 43
# Example Output 1
# This is an odd number.
# Example Input 2
# 94
# Example Output 2
# This is an even number.
# e.g. When you hit run, this is what should happen:



# Hint
# All even numbers can be divided by 2 with 0 remainder.
# Try some using the modulo with some odd numbers e.g.
# 3 % 2

# 5 % 2

# 7 % 2

# Then try using the modulo with some even numbers e.g.

# 4 % 2

# 6 % 2

# 8 % 2

# See what's in common each time.

# Test Your Code
# Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.

# Solution
#https://repl.it/@appbrewery/day-3-1-solution

##################################################################################################

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check?"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

calc = number % 2

if calc == 0:   # if number % 2 == 0
    print("This is an even number")
else:
    print("This is an odd number")

# Solution of Teacher
#
#If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
  print("This is an even number.")
#Otherwise (number cannot be divided by 2 with 0 remainder).
else:
  print("This is an odd number.")
