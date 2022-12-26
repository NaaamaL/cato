#!/usr/bin/python3
import json
import sys

def count_characters(filename):
    """
    Count the number of times each letter and digit appears in a file.
    
    Parameters:
    filename (str): The name of the file to process.
    
    Returns:
    dict: A dictionary with the counts of each letter and digit.
    """
    # Initialize a dictionary to store the counts
    counts = {}
    
    # Open the file in read mode
    with open(filename, 'r') as infile:
        # Loop through each line in the file
        for line in infile:
            # Loop through each character in the line
            for char in line:
                # Check if the character is a letter or a digit
                if char.isalpha() or char.isdigit():
                    # Increment the count for the character
                    if char in counts:
                        counts[char] += 1
                    else:
                        counts[char] = 1
    
    # Return the dictionary with the counts
    return counts

# Count the characters in the 'input.txt' file
counts = count_characters(sys.argv[1])

# Write the counts to a JSON file
with open('counts.json', 'w') as outfile:
    json.dump(counts, outfile, indent=4)
