print("You have 0 coins.")
want_coins = input("Do you want another?  ")
total_coins = 0
while want_coins == "yes":
  if want_coins == "yes":   
    total_coins += 1
    print("You have ", total_coins, "coins")
    want_coins = input("Do you want another?  ")
    
print("bye")