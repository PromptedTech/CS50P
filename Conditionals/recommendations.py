def main():
    # Ask the user how hard they want the game to be
    difficulty = input('Difficult or Casual? ')

    # If the input is neither option, tell the user and stop the program
    if not (difficulty == 'Difficult' or difficulty == 'Casual'):
        print('Enter a vaild difficulty!')
        return  # return exits the function early so nothing else runs

    # Ask the user if they want to play alone or with others
    players = input('Multiplayer or Single-player? ')

    # Same validation — only accept the exact two options
    if not (players == 'Multiplayer' or players == 'Single-player'):
        print('Enter a valid number of players!')
        return

    # Pick a game based on the combination of difficulty and player count
    if difficulty == 'Difficult' and players == 'Multiplayer':
        recommend('Poker')
    elif difficulty == 'Difficult' and players == 'Single-player':
        recommend('Klondike')
    elif difficulty == 'Casual' and players == 'Multiplayer':
        recommend('Hearts')
    else:
        recommend('Shadow Fight')


def recommend(game):
    # Print the recommended game name
    print('You might like', game)


main()
