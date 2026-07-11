def convert(text):
    # Replace text emoticons with actual emoji characters
    text = text.replace(':)', '🙂')   # happy face
    text = text.replace(':(', '🙁')   # sad face
    return text


def main():
    # Ask the user to type something with emoticons
    text = input('Type your emoticon: ')

    # Convert the emoticons and print the result
    print(convert(text))


main()
