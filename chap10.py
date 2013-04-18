#This is where the answers to Chapter 10 questions for the BSS     Dev RampUp go
# Name: Elizabeth Tenorio

 #Ex. 10.7
print "This program takes two strings and returns True if they are anagrams"

# Sort the letters in a given word
def sort_string(word):
    new_word = list(word)
    new_word.sort()
    new_word = ''.join(new_word)
    return new_word

# Compare the sorted words to check for anagrams
def is_anagram(first, second):
    sortf = sort_string(first.lower())
    sorts = sort_string(second.lower())
    if sortf == sorts:
        return True
    else:
        return False

print is_anagram('star', 'rats')
print is_anagram('dog', 'cat')
print is_anagram('Star', 'Rats')


# Ex. 10.13
# Write a program that finds all pairs of words that interlock

def interlocked(first, second):
    third = []
    f = list(first.lower())
    s = list(second.lower())
    f = list(reversed(f))
    s = list(reversed(s))
    for i in range(len(f)):
        third += f.pop()
        third += s.pop()
    thirdword = ''.join(third)
    print thirdword

    for line in open('words.txt'):
        #print line
        allwords = line.strip().lower()
        #print allwords
        if thirdword == allwords:
            return True
            break

#print interlocked('dogs', 'cats')
print interlocked('shoe', 'cold')
print 'Done!'    
    

# Can you find any words that are three-way interlocked; that is, every third letter forms a word, starting from the first, second or third?
