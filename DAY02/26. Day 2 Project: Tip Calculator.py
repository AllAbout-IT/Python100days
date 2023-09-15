# https://replit.com/@appbrewery/tip-calculator-end
# https://docs.google.com/forms/d/e/1FAIpQLSdwbmx2whgRNiciYXiSs2lJT6-dOYgvqGnXdVqfLv1fjln7kw/viewform
# https://docs.python.org/3/tutorial/floatingpoint.html
# https://www.udemy.com/course/100-days-of-code/learn/lecture/17841394#questions/13315048
# https://replit.com/@appbrewery/tip-calculator-start?v=1

total = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
person = float(input("How many people to split the bill?"))
separate = (total * (1 + (tip/100))) / person
print("Each person should pay: $" + str("{:.2f}".format(round(separate, 2))))
print(f"Each person should pay: ${round(separate, 2)}")

################################################################################

# Solution of Teacher

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)
final_amount = "{:.f2}".format(bill_per_person, 2)


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${final_amount}")