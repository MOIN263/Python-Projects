
import random
# function to specify the behaviour of the dice 
def Roll():
    a = random.randint(1, 6)
    return a

sum = 0
# the below code calculates the scores 
# As the game is the person can roll the until the turn comes as one.
while True:
    value = Roll()
    if value == 1:
        print("turn over")
        break
    else:
        sum += value

print(sum)

