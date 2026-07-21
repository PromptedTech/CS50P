def main():
    #we created a dict where we entered all the key nd da values so tht later we can use them in our program!
    items = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }


    try:
        # creating a variable w da value of 0, so tht we can later add the values inside it and use it to print the output!
        total = 0


        for item in items:
            # prompting the user for an input
            item = input('Item: ').title()
            # creating an if statement so tht if the item is in dict then we can use tht items value and then increment it in our total variable!
            if item in items:
                total += items[item]
                # now after incrementing our variable we r using it to output our total price in dollars
                print(f"Total: ${total:.2f}")
                continue
            else:
                continue

    # if the user inputs control-d, we r printing a new line so tht the user's cursor dosent remain on da same line as our program's own prompt and then end da program!
    except EOFError:
        print('')


main()
