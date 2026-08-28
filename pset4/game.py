# importing da random module
import random

# creating a infinite loop
while True:
    try:
        # asking da user to input a lvl!
        lvl = int(input('Level: '))
        # now if the lvl is greater than 0 than this loop will break
        if lvl > 0:
            break
    # and we have used exceptions, so tht if smone tries to enter lets say cat or sm bs so da program prompts 'em again for lvl!
    except ValueError:
        pass

# using the random module to pick a num between 1 and the num user stored in da lvl
num = random.randint(1, lvl)

while True:
    try:
        # getting da users guess
        guess = int(input('Guess: '))
        if guess <= 0:
            continue
    # using exceptions again
    except ValueError:
        continue

    if guess < num:
        print('Too Small!')
    elif guess > num:
        print('Too Large!')
    else:
        print('Just right!')
        break
