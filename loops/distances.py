distances = {
    'Voyager 1': 163,
    'Voyager 2': 136,
    'Pioneer': 80,
    'New Horizons': 58,
    'Pioneer 11': 44
}

def main():
    for distance in distances.values():
        print(f'{distance} AU is equal to {convert(distance)}m')

def convert(au):
    return au * 149,597,870,700

main()