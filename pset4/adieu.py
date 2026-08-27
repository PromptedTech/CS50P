import inflect

p = inflect.engine()

try:
    names = []

    while True:
        name = input('Enter a name: ')
        names.append(name)

except EOFError:
     print(f"Adieu, adieu to {p.join(names)}")