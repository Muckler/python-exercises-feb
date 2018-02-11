play_more = True

def play(player):
    answer = input("Do you want to play again? (y or n)  ")
    if answer == "y":
      return player
    elif answer == "n":
      print("Ok we're done.")
      global play_more 
      play_more = False
      return play_more
  
    else:
      print("Invalid input. ")
while play_more == True:
  play(play_more)

      
      
