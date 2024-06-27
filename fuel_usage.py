def main():
        start = float(input("What is the start odometer value in U.S miles? "))
        end = float(input("What is the end odometer value in U.S miles? "))
        fuel = float(input("What is the fuel amount in gallons? "))
        mpg = miles_per_gallon(start, end, fuel)
        lp100k = lp100k_from_mpg(mpg)
        print()
        print(f"The miles per gallon is: {mpg:.1f}")
        print(f"The litres per 100 kilometers is: {lp100k:.2f}")
        pass

def miles_per_gallon(start_miles, end_miles, amount_gallons):
        """Compute and return the average number of miles
        that a vehicle traveled per gallon of fuel.
        Parameters
            start_miles: An odometer value in miles.
            end_miles: Another odometer value in miles.
            amount_gallons: A fuel amount in U.S. gallons.
        Return: Fuel efficiency in miles per gallon.
        """
        mpg = (end_miles - start_miles) / amount_gallons

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