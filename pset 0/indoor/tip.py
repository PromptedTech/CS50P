def main():
    # Ask how much the meal cost and what tip percentage to leave
    dollars = dollors_replace(input("How much was the meal? "))
    percent = percent_replace(input("What percentage would you like to tip? "))

    # Multiply meal cost by tip percentage to get the tip amount
    tip = dollars * percent

    # Print the tip with exactly 2 decimal places (like money, e.g. $3.75)
    print(f"Leave ${tip:.2f}")


def dollors_replace(d):
    # Remove the "$" sign so we can convert the text to a number
    # e.g. "$50.00" becomes 50.0
    return float(d.replace("$", ""))


def percent_replace(p):
    # Remove the "%" sign and divide by 100 to convert to a decimal
    # e.g. "15%" becomes 0.15
    return float(p.replace("%", "")) / 100


main()
