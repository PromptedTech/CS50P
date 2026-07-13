import sys

def main():
    # so why use a tuple?
    # Welp agn if u r very sure u wont be changing values or adding to them, but u r sure you want to be efficient w memory,
    # this is a great way to represent your data!
    # this diff of 20 or so bytes could really pay off over millons and millons of rows in ur data or millons of millons of ppl who r sharing their coordinates!
    coordinates_tuples = (42.376, -71.115)
    coordinates_list = [42.376, -71.115]
    print(f'{sys.getsizeof(coordinates_tuples)} bytes')
    print(f'{sys.getsizeof(coordinates_list)} bytes')

main()