def main():
    # Ask the user to enter a number and convert it from text to an integer
    x = int(input("Whats x? "))

    # Call is_even() to check and print whether the number is even or odd
    if is_even(x):
        print("Even")
    else:
        print('Odd')


def is_even(n):
    # A number is even if dividing by 2 leaves no remainder (remainder == 0)
    return n % 2 == 0


main()
