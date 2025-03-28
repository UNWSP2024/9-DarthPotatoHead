#Program Written By: Ainsley Bellamy
#Date Written: 03/27/2025
#Program Title: Write_Numbers


# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

import random

#Function to write numbers to the numbers.txt files; user chooses number of numbers.
def main():
    try:
#Get loop (i.e., number of numbers) runtime from user.
        numRange = int(input("How many random numbers would you like written to the file numbers.txt? "
                             "Enter a number from 1 up to 1000: "))
#Input handling.
        while numRange < 1 or numRange > 1000:
            numRange = int(input("INVALID INPUT -- Number cannot be less than zero or greater than 1000. "
                             "Enter a number up to 1000: "))
#Open file for writing and for the number the user specified write a number between 1-500 to numbers.txt.
        with open('numbers.txt', 'w') as numberFile:
            for i in range(numRange):
                randomNum = str(random.randint(1,501))
                numberFile.write(f'{randomNum}\n')
#Confirm to user.
            print(f"{numRange} numbers were written to the numbers.txt file.")
#Error handling.
    except ValueError as err:
        print(err)
    except:
        print("An Error Occurred")

if __name__ == '__main__':
    main()
