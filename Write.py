# Write random numbers to a file. The user specifies how many numbers to write.
# The numbers should be from 1 through 500.
# Chris Blaylock
# 10/20/2019

# Import the random library
import random
try:
    # Open the file
    outfile = open ('random_numbers.txt', 'w')
    # Input from the user specify how many random numbers to generate.
    Number_of_Random_Numbers = int(input("How many random numbers do you want to generate?"))


    # Use a loop to generate the number of random numbers requested by the user

    for num in range (Number_of_Random_Numbers):
        number = random.randint(1,500)
        # Output: write the random numbers to a file
        outfile.write(str(number) + '\n')

    # Close the file
    outfile.close()
    
except IOError:
    print("An error occurred trying to open the file")

except Exception as err:
    print(err)
