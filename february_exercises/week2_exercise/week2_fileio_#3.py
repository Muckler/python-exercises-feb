user_in = input('Enter a file name..  ')
file_handle = open(user_in, 'r')
contents = file_handle.read()
lower_contents = contents.lower()
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
def word_histogram(paragraph):
    the_words = ""
    word_list = []
    word_dict = {}
    for i in range(len(paragraph)):
      if i == len(paragraph) - 1:
        the_words = the_words + paragraph[i]
        word_list.append(the_words)
        #the_words = ""
      elif paragraph[i] != " ":
        the_words = the_words + paragraph[i]
      elif paragraph[i] == " ":
        word_list.append(the_words)s
        the_words = ""
      
    for each in word_list:
        word_dict.update({each:0}) 
    for each in word_list:s
        word_dict[each] += 1
    return word_dict

print(letter_histogram(lower_contents))
print(word_histogram(lower_contents))



