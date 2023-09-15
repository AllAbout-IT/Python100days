# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


names = name1 + name2
lower_names = names.lower()

t_count = lower_names.count("t")
r_count = lower_names.count("r")
u_count = lower_names.count("u")
e_count = lower_names.count("e")

l_count = lower_names.count("l")
o_count = lower_names.count("o")
v_count = lower_names.count("v")

true_num = t_count + r_count + u_count + e_count
love_num = l_count + o_count + v_count + e_count

total_num = int(str(true_num)+str(love_num))

if total_num <= 10 or total_num >= 90:
    print(f"Your score is {total_num}, you go together like coke and mentos.")
elif total_num >= 40 and total_num <= 50:
    print(f"Your score is {totla_num}, you are alright together.")          
else:
    print(f"Your score is {total_num}") 
