# 24. Number Manipulation and F Strings in Python

print(8/3)
#   - It will be the float

print(int(8/3))
#   - And, You can change this other types.

print(round(8 / 3, 2))
#      (function) def round(
#           number: _SupportsRound1[_T@round],
#           ndigits: None = None
#           ) -> _T@round 

print(round(8 // 3))
#       - If you want just only Integer in result , just put '/' one more.

score = 2

score -= 2
print("1. = " + str(score))
score += 2
print("2. = " + str(score))
score *= 2
print("3. = " + str(score))
score /= 2
print("4. = " + str(score))

############################################################################

# F-string
score = 0
height = 1.8
isWinning = True

print("your score is " + str(score))
# or You can write it as next way.
print(f"your score is {score}, your height is {height}, your are winning is {isWinning}")
#       Using f before "" can that skip writing type before parameter.

