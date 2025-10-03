#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies



import re


def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if not text[0].isupper():   
        return False
    if not re.search(r'[.!?]$', text):   
        return False
    if not re.search(r'\w', text):   
        return False
    return True


user_sentence = input("Enter a sentence: ")

while is_sentence(user_sentence) == False:
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")


words = re.findall(r'\b\w+\b', user_sentence.lower())

unique_words = []
frequencies = []


for word in words:
    if word in unique_words:
        index = unique_words.index(word)
        frequencies[index] += 1
    else:
        unique_words.append(word)
        frequencies.append(1)


print("\nWord Frequencies:")
for i in range(len(unique_words)):
    print(unique_words[i] + ":", frequencies[i])
