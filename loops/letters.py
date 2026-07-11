def main():
    print(write_letter('Mario', 'Princess Peach'))
    print(write_letter('Luigi', 'Princess Peach'))
    print(write_letter('Daisy', 'Princess Peach'))
    print(write_letter('Yoshi', 'Princess Peach'))

def write_letter(reciver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {reciver}, 

        You r cordially invited to a ball at
        Peach's Castle ts evening, 7:00 PM.

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

main()
