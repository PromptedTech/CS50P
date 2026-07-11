# Ask the user the famous question from "The Hitchhiker's Guide to the Galaxy"
# strip() removes extra spaces, lower() makes it case-insensitive
question = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').strip().lower()

# Accept the answer written as a number or spelled out in words
if question == '42' or question == 'forty two' or question == 'forty-two':
    print('Yes')
else:
    print('No')
