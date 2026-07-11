# Ask the user for their name
name = input('Whats your name? ')

# Use a match statement (like a switch in other languages) to assign a Hogwarts house
match name:
    case 'Harry' | 'Hermoine' | 'Ron':
        # These three characters all belong to Gryffindor
        print('Gryffindor')
    case 'Draco':
        print('Slytherin')
