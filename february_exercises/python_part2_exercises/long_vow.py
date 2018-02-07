my_str = input("Enter a word with two vowels next to eachother..   ")
two_vowels = ["ee", "oo"]
new_str = ""
for i in range(0, len(my_str)):
  if my_str[i:i+2] in two_vowels:
    new_str = my_str[0:i] + (my_str[i] * 4) + my_str[i+3:]
  else:
    new_str = new_str + my_str[i]

print(new_str)