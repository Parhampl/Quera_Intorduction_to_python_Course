'''
get a word as input and then tell what number is this letter in alphabet.
'''
first_letter = ord('a')
desired_letter_ascii = ord(input())
# desired_letter_ascii = ord(desired_letter)
print(desired_letter_ascii-first_letter+1)
