#!/usr/bin/python3

import sys

def generate_solution(riddlefile, solutionfile):
    """
    Generate a solution to a riddle based on the numbers in a text file.
    
    The function reads a text file with a list of numbers, and writes the solution
    to another text file. If a number is divisible by both 5 and 3, the solution
    is "GollumSmeagol". If the number is divisible by 5, the solution is "Gollum".
    If the number is divisible by 3, the solution is "Smeagol". If the number is
    not divisible by either 5 or 3, the original number is written to the solution
    file.
    
    Parameters:
    riddlefile (str): The name of the riddle file.
    solutionfile (str): The name of the solution file.
    """
    # Open the text file in read mode
    with open(riddlefile, 'r') as infile:
        # Open the text file in write mode
        with open(solutionfile, 'w') as outfile:
            # Loop through each line in the riddlefile
            for line in infile:
                # Convert the line to string
                number = int(line)

                # Check if the number is divisible by 5 and 3
                if number % 5 == 0 and number % 3 == 0:
                    outfile.write("GollumSmeagol\n")
                # Check if the number is divisible by 5
                elif number % 5 == 0:
                    outfile.write("Gollum\n")
                # Check if the number is divisible by 3
                elif number % 3 == 0:
                    outfile.write("Smeagol\n")
                # If the number is not divisible by 5 or 3
                else:
                    outfile.write(line)
                    
generate_solution(sys.argv[1], sys.argv[2])
