# Multiple If Statements in Succession
#
# e.g.
#
# in condition1:
#   do A
# if condition2:
#   do B
# if condition3:
#   do C
#
# e.g.
# https://app.diagrams.net/?lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%204#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1aoRTeFOb2SJO7ofMnhTCneCEboHowF2A%26export%3Ddownload
# https://replit.com/@appbrewery/day-3-multiple-if
# 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!") 
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("please pay $7.")
    else:
        bill = 12
        print("please pay $12.")
    
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
         bill += 3

    print(f"your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
