
# Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter.
# Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes a hyphen will separate the two letters in the string.

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#get user input
user_range = input("Enter a range of letters (e.g., a-z): ")

#identify location
start_letter, end_letter = user_range.split("-")
start_alphabet = alphabet.index(start_letter[0])
end_alphabet = alphabet.index(end_letter[-1])

#get range of the letter
result_string = alphabet[start_alphabet:end_alphabet + 1]

#print result
print(result_string)
