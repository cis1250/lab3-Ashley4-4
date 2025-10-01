#!/usr/bin/env python3

# Word frequency exercise

import re

# Function that checks if a text qualifies as a sentence
def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if not text[0].isupper():
        return False
    if not re.search(r'[.!?]$', text):
        return False
    if not re.search(r'\w+', text):
        return False
    return True

user_sentence = input("Enter a sentence: ")

while not is_sentence(user_sentence):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

# Split sentence
words = user_sentence.split()

# make lists for the words and their frequencies
unique_words = []
word_frequencies = []

# Process words and count frequencies
for word in words:
    # make all of the words lowercase
    word = word.lower()
    # remove punctuation at the end of the word
    if word[-1] in ".!?,":   
        word = word[:-1]
    # check if the word is already in the list
    if word in unique_words:
        index = unique_words.index(word)
        word_frequencies[index] += 1
    else:
        unique_words.append(word)
        word_frequencies.append(1)

# Print results
print("\nWord Frequencies:")
for i in range(len(unique_words)):
    print(f"{unique_words[i]}: {word_frequencies[i]}")
