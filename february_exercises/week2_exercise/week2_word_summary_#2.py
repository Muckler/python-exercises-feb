enter_paragraph = ("To be or not to be")  
user_paragraph = enter_paragraph.lower()
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
        word_list.append(the_words)
        the_words = ""
      
    for each in word_list:
        word_dict.update({each:0}) 
    for each in word_list:
        word_dict[each] += 1
    return word_dict
              
    # adding each letter from alphabet to dictionary
print(word_histogram(user_paragraph)) 