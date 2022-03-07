def main():
    # Get an odometer value in U.S. miles from the user.
    start_miles = float(input('Enter the first odometer reading (miles): (30462)'))

    # Get another odometer value in U.S. miles from the user.
    end_miles = float(input('Enter the second odometer reading (miles): (30810)'))

    # Get a fuel amount in U.S. gallons from the user.
    amount_gallons = float(input('Enter the amount of fuel used (gallons): (11.2)'))

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)
    # Display the results for the user to see.
    print(f'{mpg:.1f} Miles per gallon')
    print(f"{lp100k:.2f} liters per 100 kilometers")
    pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    mpg = abs(end_miles - start_miles) / amount_gallons
    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp100k = 235.215 / mpg
    return lp100k


# Call the main function so that
# this program will start executing.
main()


