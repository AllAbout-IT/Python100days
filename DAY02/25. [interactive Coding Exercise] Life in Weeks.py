# https://waitbutwhy.com/2014/05/life-weeks.html
# https://app.codingrooms.com/management/assignments/364911/overview

# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# https: // waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56

# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

# e.g. When you hit run, this is what should happen:

#########################################################

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

yearsoflife=90
# monthsofyear=12
# weeksofyear=52
# daysofyear=365
restoflife=int(yearsoflife)-int(age)

restofdays=restoflife*365
restofweeks=restoflife*52
restofmonths=restoflife*12a

print(f"You have {restofdays} days, {restofweeks} weeks, and {restofmonths} months left")

##############################################

# teacher's answer
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left"
print(message)
