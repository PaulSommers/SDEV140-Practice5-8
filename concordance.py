"""
Author: Paul Sommers
Date written: 11/11/2024
Assignment: Exercise 5-8 - Concordance
Short Desc: This program reads a text file, counts the frequency of each unique word, and prints the words and their frequencies in alphabetical order.
"""

# Get the file name
file = input("Enter the input file name: ")

# Initialize an empty dictionary for unique words and frequencies
uniqueWords = {}

# Open the file for reading
with open(file, 'r') as f:
    
    # Loop through each line in the file
    for text in f:
        
        # Split the line into words
        wordList = text.split()
        
        # Loop through each word in the line
        for word in wordList:
            
            # If the word is already in the dictionary, increment its frequency
            if word in uniqueWords:
                uniqueWords[word] += 1
                
            else:
                # If the word is not in the dictionary, add it
                uniqueWords[word] = 1

# Sort the words alphabetically
sortedWords = sorted(uniqueWords)

# Print each unique word and its frequency
for word in sortedWords:
    print(f"{word} {uniqueWords[word]}")