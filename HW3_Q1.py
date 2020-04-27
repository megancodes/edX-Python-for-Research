import string

# Exercise 1
# Create a string called alphabet consisting of the space character ' '
# followed by (concatenated with) the lowercase letters. Note that we're only using the lowercase letters in this exercise.
alphabet = ' ' + string.ascii_lowercase

# Exercise 2
# Create a dictionary with keys consisting of the characters in alphabet
# and values consisting of the numbers from 0 to 26.
# Store this as positions.
positions = {}
length = len(alphabet)
for i in range(length):
    positions[alphabet[i]] = i
    # positions[i] = alphabet[i]
print(positions)


# Exercise 3
# Use positions to create an encoded message based on message where each
# character in message has been shifted forward by 1 position, as defined by positions.
# Note that you can ensure the result remains within 0-26 using result % 27
# Store this as encoded_message.
CIPHER = 1
encoded = {alphabet[i]: ((i + CIPHER) % length) for i in range(length)}
# encoded = {((i + key) % length): alphabet[i] for i in range(27)}
print(encoded)

message = "hi my name is caesar"
encoded_message = " "
for letter in message:
    encoded_message = alphabet[encoded[letter]]
    print(encoded_message, end = "")
print()
   # print((positions[letter] + CIPHER) % length)


# Exercise 4
# Define a function encoding that takes a message as input as well as an int
# encryption key key to encode a message with the Caesar cipher by shifting
# each letter in message by key positions.
# Your function should return a string consisting of these encoded letters.
# Use encoding to encode message using key = 3 and save the result as encoded_
# message. Print encoded_message.
def encoding(message, key):
    encoded = {alphabet[i]: ((i + key) % length) for i in range(length)}
    encoded_message = ""
    for letter in message:
        encoded_message += alphabet[encoded[letter]]
    return encoded_message

key = 3
encoded_message = encoding(message, key)
print(encoded_message)

# Exercise 5
# Use encoding to decode encoded_message.
# Store your encoded message as decoded_message.
# Print decoded_message. Does this recover your original message?
new_key = -3
decoded_message = encoding(encoded_message, new_key)
print(decoded_message)
# Yes recovers original message