#Program Written By: Ainsley Bellamy
#Date Written: 03/27/2025
#Program Title: Get_NumNames


# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

#Function to count the names (lines) in the names.txt file.
def count_file_lines():
#Open for reading.
    nameFile = open('names.txt', 'r')
#Readlines and take the length.
    nameCounter = len(nameFile.readlines())
    nameFile.close()
#Display to user.
    print(f'There are {nameCounter} name(s) in the names.txt file.')

# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()

#There are a lot of ways to do this!
#####
    # nameCounter = [name for name in nameFile]
    # nameCounter = len(nameCounter)
#####
    # nameCounter = 0
    # for name in nameFile:
    #     nameCounter += 1