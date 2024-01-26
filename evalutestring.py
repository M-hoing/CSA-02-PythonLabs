
# Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter.
# Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes a hyphen will separate the two letters in the string.

alphabet = "abcdefghijklmnopqrstuvwxyz"
user_range = input("Enter a range of letters (e.g., a-z): ")


start_letter, end_letter = user_range.split("-")
start_alphabet = alphabet.index(start_letter.lower())
end_alphabet = alphabet.index(end_letter.lower())

result_string = alphabet[start_alphabet:end_alphabet + 1]

result_string = result_string.upper() * start_letter.isupper() + result_string.lower() * start_letter.islower()

print(result_string)
