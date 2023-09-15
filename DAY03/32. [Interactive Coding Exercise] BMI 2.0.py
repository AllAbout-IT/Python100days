# https://app.codingrooms.com/management/assignments/364916/overview

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# BMI = weight(kg) / height²

# The testing code will check for print output that is formatted like one of the lines below:

# "Your BMI is 18, you are underweight."
# "Your BMI is 22, you have a normal weight."
# "Your BMI is 28, you are slightly overweight."
# "Your BMI is 33, you are obese."
# "Your BMI is 40, you are clinically obese."

##################################################################

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = round(weight / (height ** 2))

if BMI < 18.5:
    print(f"your BMI is {BMI}, you are underweight.")
elif 18.5 < BMI < 25:
    print(f"your BMI is {BMI}, you have a normal weight.")
elif 25 < BMI < 30:
    print(f"your BMI is {BMI}, you are slightly overweight.")
elif 30 < BMI < 35:
    print(f"your BMI is {BMI}, you are you are obese.")
elif BMI > 35:
    print(f"your BMI is {BMI}, you are clinically obese.")

######################################################################

# Solution of Teacher

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:                      # You don't have to put '18.5 > bim' because if the value(BMI) is out from 'if', the process will skip to the next 'elif'.
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

