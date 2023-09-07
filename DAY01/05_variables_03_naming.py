# the rules for variable's naming

# Rule.01 you can't use space between strings. for example 'hostname' have no problem. but 'host name' will be error. if you want to separate words, use '_(under bar)' between words like 'host_name'

# Rule.02 All kinds of numbers couldn't be the first place in names for example '1host', '10name'


#Assignment

#1. Create a greeting for your grogram.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Mke sure the input cursor shows on a new line, see the example at.

print('Hello everyone! I can help you to make band naming')
city_name = input('what city did you grow up in when you were little\n?? ')
pet_name = input('what is your pet name?\n')
print('Your best band name is '+ city_name + pet_name)

# \n will change to next line


