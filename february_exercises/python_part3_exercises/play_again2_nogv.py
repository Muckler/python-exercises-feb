##can't get this to work without global variable
def play():
    player = True
    answer = input("Do you want to play again? (y or n)  ")
    if answer == "y":
      return player
    elif answer == "n":
      print("Ok we're done.") 
      player = False
      return player
    else:
      print("Invalid input. ")
      return player
while True:
  play()

      
      
