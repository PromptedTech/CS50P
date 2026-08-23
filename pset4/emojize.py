import emoji

emoji_language = input('Input: ')

def main():
    print(emoji.emojize(emoji_language, language='alias'))

main()