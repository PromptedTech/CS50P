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
    # Print the value of x if it was successfully converted to an integer
    print(f'x is {x}')