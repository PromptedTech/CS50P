def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date = input('Dates: ').strip()

        try:
        
            if '/' in date:
                month, day, year = date.split('/')
                
                month = int(month)
                day = int(day)
                year = int(year)

            else:
                month, day, year = date.split(' ')

                if month not in months or not day.endswith(','):
                    raise ValueError

                month = months.index(month) + 1
                day = int(day[:-1])
                year = int(year)
            
            if 1 <= month <= 12 and 1 <= day <= 31:
                break

        except (ValueError, IndexError):
            pass
        
    print(f"{year:04}-{month:02}-{day:02}")

main()