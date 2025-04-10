#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: April 10, 2025

# Factorial program in python


def warn_input(reason, output):
    match reason:
        case "Decimal":
            print("Please don't enter a decimal")
        case "Negative":
            print("Please enter a positive number greater than or equal to 0")
        case "String":
            print("Please enter an integer!")
    print("You entered:", output)


def main():
    factorial_number = 1
    counter = 0

    user_number = input("Enter a positive integer: ")

    try:
        user_number = float(user_number)

        # Warn user based on input
        if user_number == int(user_number) and user_number >= 0:

            # If user number is valid
            while True:
                counter += 1
                factorial_number *= counter
                print("Tracking {} times through loop".format(counter))
                if counter >= user_number:
                    break

            print("The factorial of your number is ", factorial_number)
        elif user_number < 0:
            warn_input("Negative", user_number)
        else:
            warn_input("Decimal", user_number)
    except:
        warn_input("String", user_number)


if __name__ == "__main__":
    main()
