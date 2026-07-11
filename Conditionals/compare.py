# Ask the user to enter two numbers and convert them from text to integers
x = int(input('Enter a number: '))
y = int(input('Enter another number: '))

# Compare x and y and print which one is bigger, or if they are equal
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
