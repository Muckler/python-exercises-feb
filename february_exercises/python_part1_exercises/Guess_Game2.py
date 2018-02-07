import random
guess = random.randint(1, 10)
gotit = False
while gotit != True:
  print("My guess is...  ", guess) 
  answer = input("Is that it? (y or n)")
  if  answer == "y":
    print("I'm pretty smart")
    gotit = True
  elif answer == "n":
    goit = False
    guess = random.randint(1, 10)

    

  