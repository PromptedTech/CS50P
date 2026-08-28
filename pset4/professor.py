import random


def main():
    score = 0
    level = get_level()

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        
        correct = False

        for i in range(3):
            question = int(input(f'{x} + {y} = '))

            if question == x + y:
                score += 1
                correct = True
                break
            else:
                print('EEE')

        if correct == False:
            print(f"{x} + {y} = {x + y}")

    print(score)


def get_level():
    while True:
        lvl = int(input('Tell us the level u want to ply is brotha(1, 2 or 3): '))
        if lvl > 3:
            continue
        elif lvl <= 0:
            continue
        else:
            return lvl


def generate_integer(lvl):
    if lvl == 1:
        num = random.randint(0, 9)
        return num
    elif lvl == 2:
        num = random.randint(10, 99)
        return num
    elif lvl == 3:
        num = random.randint(100, 999)
        return num
    else:
        raise ValueError


if __name__ == "__main__":
    main()