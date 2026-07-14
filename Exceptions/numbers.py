def main():
    x = get_int()
    print(f'x is {x}')

def get_int():
    while True:
    # Try to convert user input to an integer
        try:
            # Prompt user for input and convert it to an integer
            x = int(input('Whats x? '))

        # Handle the case where user input cannot be converted to an integer
        except ValueError:
            # Print error message if the input is not a valid integer
            print('x is not an integer!')

        # If no exception occurred, the conversion was successful
        else:
            break
        
    return x

main()