# Read a file with an unknown number of numbers in it
# Calculate and display the total of the numbers and the number of numbers
# in the file
# Chris Blaylock
# 10/30/2019

# Initialize variables
total = 0
count = 0

# Input: read numbers from a file

# Handle any exceptions using try/except
try:
    
    # Open the file
    infile = open('random_numbers', 'r')

    for num in infile:
        number = int(num)
        total = total + number
        count = count + 1

    # Close the file
    infile.close()


    # Output: display the total of the numbers, and the number of numbers
    print("The total of the random numbers is", total)
    print("The number of random numbers in the file is", count)

except IOError:
    print("An error occurred trying to open the file")

except ValueError:
    print("Non-numeric data found in the file")

except Exception as err:
    print(err)

