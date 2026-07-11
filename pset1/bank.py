# Ask the user to type a greeting
greeting = input('Greeting: ')

# Remove extra spaces from both ends and convert everything to lowercase
# so "  Hello " becomes "hello" — makes comparing easier
greeting = greeting.strip().lower()

# Give $0 if they say hello (best greeting)
if greeting.startswith('hello'):
    print('$0')
# Give $20 if they start with "h" but not "hello" (e.g. "hey", "howdy")
elif greeting.startswith('h'):
    print('$20')
# Give $100 for any other greeting (e.g. "what's up", "yo")
else:
    print('$100')
