def main():
    # Ask the user for a number and convert it from text to an integer
    x = int(input("What is x? "))

    # Call the square function and print the result
    print('x squared is', square(x))


def square(n):
    # Multiply the number by itself to get the square (e.g. 4 * 4 = 16)
    return n * n


main()
