SHOWS = [
    'Avatar: the way of water',
    '   jimmy neutron',
    '  the proud family   ',
    'kim possible',
    '  spongebob squarepants'
]

def main():
    cleaned_show = []
    for show in SHOWS:
        cleaned_show.append(show.strip().title())

    print(', '.join(cleaned_show))

main()