import requests

def main():
    print('Search the Art Institute of Chicago!')
    artist = input("Artist: ")

    try:
        responce = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {'q': artist}
            )
        responce.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        return

    content = responce.json()
    for artwork in content["data"]:
        print(f'{artwork['title']}')


main()