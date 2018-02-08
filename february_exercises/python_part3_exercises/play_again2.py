def first_play():
  def play():
    answer = input("Do you want to play again? (y or n)  ")
    if answer == "y":
      return True
    elif answer == "n":
      return False
    else:
      print("Invalid input. ")
      first_play()
    

print(play())