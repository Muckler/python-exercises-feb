def play():
  answer = input("Do you want to play again? (y or n)  ")
  if answer == "y":
    return True
  elif answer == "n":
    return False

print(play())

