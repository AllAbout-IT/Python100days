# Example Input
# 39
# 
# Example Output
# 3 + 9 = 12
# 12

# Hint
# 1. Try to find out the data type of two_digit_number.
# 2. Think about what you learnt about subscripting.
# 3. Think about type conversion.

# num = input("Type a two digit number: ")
# result = int(num[0]) + int(num[1])
# print(result)

############################################################################################################

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

result = int(two_digit_number[0]) + int(two_digit_number[1])
print(result)

# teacher's answer

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result1 = int(first_digit) + int(second_digit)

print(type(first_digit))
