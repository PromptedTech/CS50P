def main():
    while True:
        
        try:
            x, y = map(int, input('Fraction: ').split('/'))

            if y == 0:
                continue
            if x > y:
                continue
            if x < 0:
                continue
            if y < 0:
                continue

            percentage = round(x / y * 100)

            if percentage <= 1:
                print('E')
            elif percentage >= 99:
                print('F')
            else:
                print(f'{percentage}%')

            break

        except (ValueError, ZeroDivisionError):
            continue

main()