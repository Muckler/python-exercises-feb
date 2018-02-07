secret_num = 5
print("I am thinking of a number between 1 and 10")
guess = int(input("What's the number?  "))
while guess != secret_num:
  print("Nope, try again")
  guess = int(input("What's the number?  "))
print("Yes! You win!")