# Exercise 1
# counting number of letters in a sentence
import string

alphabet = string.ascii_letters

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}

for letter in sentence:
    if letter not in count_letters:
        count_letters[letter] = 1
    else:
        count_letters[letter] += 1

def counter(input_string):
    print(count_letters)

counter(sentence)



