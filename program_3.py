#Program Written By: Ainsley Bellamy
#Date Written: 03/27/2025
#Program Title: Sum_Numbers


# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.

#Function to read lines from numbers.txt, convert to numbers, and sum.
def sum_numbers_from_file():
    try:
        with open('numbers.txt', 'r') as numberFile:
#I was able to read the lines from numbers.txt, convert to integers, and
# sum in one line with a list comprehension.
            total = sum([int(line) for line in numberFile])
#Display to user.
            print(f'The sum of the number from numbers.txt is {total}.')
#Exception handling.
    except IOError as err:
        print('An error occurred trying to read the file:')
        print(err)
    except ValueError as err2:
        print('An error occurred when trying to sum the numbers.')
        print(err2)
#Catchall.
    except Exception as err3:
        print(f'An error occurred.\n{err3}')

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()