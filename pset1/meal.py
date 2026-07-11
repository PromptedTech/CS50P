def main():
    # Ask the user to enter the current time
    time = input("What time is it? ")

    # Convert the time string to a float (e.g. "7:30" becomes 7.5)
    hours = convert(time)

    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")


def convert(time):
    # Split the time string into hours and minutes using ":" as separator
    hours, minutes = time.split(":")

    # Convert to float: divide minutes by 60 and add to hours
    return int(hours) + int(minutes) / 60


if __name__ == "__main__":
    main()
