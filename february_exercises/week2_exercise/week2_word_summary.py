#still working on this one: but fixed it with 
#week2_word_summary_#2.py
user_paragraph = ("to be or not to be")  
user_paragraph.lower()
def word_histogram(paragraph):
    the_words = ""
    word_list = []
    word_dict = {}
    for i in range(len(paragraph)):
      if paragraph[i] != " ":
        the_words = the_words + paragraph[i]
        
      elif paragraph[i] == " ":
        word_list.append(the_words)
        the_words = ""
      elif i == len(paragraph)-1:
        the_words = the_words + the_words[i]
        word_list.append(the_words)
        #the_words = ""
    for each in word_list:
        word_dict.update({each:0}) 
    print(word_list)
    print(word_dict) 
    for each in word_list:
        word_dict[each] += 1
    return word_dict
              
    # adding each letter from alphabet to dictionary
print(word_histogram(user_paragraph)) 