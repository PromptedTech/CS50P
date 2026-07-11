def main():
    # Ask the user for a vanity plate.
    plate = input("Plate: ")

    # Print whether the plate meets all of the rules.
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # A plate must be between 2 and 6 characters long.
    if not 2 <= len(s) <= 6:
        return False

    # The first two characters must be letters.
    if not s[:2].isalpha():
        return False

    # Only letters and numbers are allowed.
    if not s.isalnum():
        return False

    # Check that any numbers appear only at the end.
    first_number_index = None
    for i, char in enumerate(s):
        if char.isdigit():
            first_number_index = i
            break

    # If there are no numbers, the plate is valid so far.
    if first_number_index is None:
        return True

    # The first number cannot be 0.
    if s[first_number_index] == "0":
        return False

    # Everything after the first number must also be numbers.
    return s[first_number_index:].isdigit()


main()