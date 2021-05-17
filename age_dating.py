#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 11, 2021
# This program decides if your age is acceptable for dating
# these peoples daughter


# define main function
def age_dater():
    # get age
    age = input("What is your age?: ")

    # make sure that the age is a number
    try:
        age = int(age)
    except ValueError:
        # if the age is not a number tell the user
        print("That is not a valid number")
        age_dater()
    # if the age is a number do the main process
    else:
        # turn age into an int
        age = int(age)

        # check is age is within the acceptable range
        if ((age > 25) and (age < 40)):
            # if it is then print this
            print("Welcome to the family")

        else:
            if (age > 40):
                # otherwise print this
                print("You are to old to date our daughter")

            elif(age < 25):
                # otherwise print this
                print("You are to young to date our daughter")


# start the main function
if __name__ == "__main__":
    age_dater()
