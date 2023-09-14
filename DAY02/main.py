print(len("Hello")) #'len' only can work in 'String'

# print(len(12345)) It isn't working
# TypeError: object of type 'int' has no len()
# 
# Data Types
# String
#   1 Every strings in '" "'  are handled as 'Strings'
#       - EX> "HELLO" 
#       - Even if these strings are "123", It is processed as 'String'
#       - EX>
print("123"+"345") # 468?
#       - The answer becomes '123345'
#       - In addition, You can combine two words through it.
print("Hello"+"python")
#       - The answer is became 'Hellopython'.
# 
#   2 We can pull out string in '" "' each
#       - EX>
print("HELLO"[2])
#       - This structure is like this
#           |0|1|2|3|4|
#           |H|E|L|L|O|
#       - We always have to know that the number in binary is started from '0'
#       - We call this 'Subscript'

# Integer
#    - All whole numbers no matter if they're positive or negative, are called integers in programming.
#    - If you want to make processing 'add' in numbers
#    - Just put numbers without anything.
#    - EX>
print(123 + 345)

# Float(Float pointing number)
#   - The numbers having decimal places are called 'Float'
#   - EX> 3.14159
#
# Boolean
#   - Boolean has only two values 'True(1)', 'False(0)'
