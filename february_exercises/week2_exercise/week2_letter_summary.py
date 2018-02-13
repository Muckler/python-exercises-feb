enter_word = input('Please enter a word:  ')
#throwing error if middle letter is upper case?
user_word = enter_word.lower()
def letter_histogram(word):
    alphabet = []
    # loop to get characters a to z
    for i in range(97, 123):
        alphabet.append((chr(i)))
    letter_dict = {}
    letter_dict = {" ": 0}
    # adding each letter from alphabet to dictionary
    for each in alphabet:
        letter_dict.update({each:0})
    for each in word:
        letter_dict[each] += 1
    return letter_dict
print(letter_histogram(user_word))

