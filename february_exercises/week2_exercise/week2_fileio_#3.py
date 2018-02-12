user_in = input('Enter a file name..  ')
file_handle = open(user_in, 'r')
contents = file_handle.read()
file_handle.close()
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
print(letter_histogram(contents))



