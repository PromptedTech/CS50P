def main():
    guests_list = [
        'Nakul',
        'Shiva',
        'Shailendra',
        'Kabeer',
        'Vihaan',
        'Rohan',
        'Jay',
    ]

    for guest in guests_list:
        print(write_letter(guest))


def write_letter(receiver):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver}, 

        You are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        Princess Peach
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

main()