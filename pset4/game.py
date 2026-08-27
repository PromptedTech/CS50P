import random

while True:
    lvl = int(input('Level: '))
    if lvl > 0:
        break

num = random.randint(1, lvl)

while True:
    guess = int(input('Guess: '))
    if guess <= 0:
        continue

    if guess < num:
        print('Too large!')
    elif guess > num:
        print('Too small!')
    else:
        print('Just right!')
        break
    