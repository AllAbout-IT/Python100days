# fuction 'input' is

# def input(
#     __prompt: object = "",
#     /
# ) -> str
# Read a string from standard input. The trailing newline is stripped.

# The prompt string, if given, is printed to standard output without a trailing newline before reading input.

# If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError. On *nix systems, readline is used if available.

# EX
input("what is your name?")

# and

# input() will get user input in console
# Then print() will print the owrd "Hello" and the user input
# print('Hello' + input("What is your name?") + "!")

# # How to get number of string's length?
# def len(
#     __obj: Sized,
#     /
# ) -> int

# Ex
print(len("Jack"))

# If you want to count string's number from input

print(len(input('what is your name? ')))

