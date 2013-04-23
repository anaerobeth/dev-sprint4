# This is where the answers to Chapter 11 questions for the BSS         Dev RampUp go
# Name: Elizabeth Tenorio

# Ex. 11.9
# Use a dictionary to write a faster, simpler version of has_duplicates.
# Solution based on group discussion during the Rampup community hours
# has_duplicates that takes a list
# and returns True if there is any element that appears more than once

lst = ['apple', 'orange', 'peach', 'peach', 'banana', 'kiwi']

def has_duplicates(lst):
    duplicates = {}
    for item in lst:
        if item in duplicates:
            return True
        else:
            duplicates[item] = 1
    return False

print has_duplicates(lst)

# Ex. 11.10
# Write a program that reads a wordlist and finds all the rotate pairs.

def rotate_word(word):
    key = 13
    new_word = ''
    s = word.lower()
    for letter in s:
        new_ord = key + ord(letter)
        if new_ord > 122:
            #lowerrcase letters can have ord from 65 to 90
            new_ord = new_ord -26
            new_letter = chr(new_ord)
        else:
            new_letter = chr(new_ord)

        new_word = new_word + new_letter

    return new_word


def rotate_pair():
    wordlist = []
    for line in open('words.txt'):
        word = line.strip()
        wordlist.append(word)
    for line in open('words.txt'):
        word = line.strip()
        pair = rotate_word(word)
        if pair in wordlist:
            print "Rotate pair found!"
            print word, pair

rotate_pair()
# Rotate pair found!
# abjurer nowhere
# Rotate pair found!
# abo nob
