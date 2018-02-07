secret_num = 5
print("I am thinking of a number between 1 and 10")
guess = int(input("What's the number?  "))
while guess != secret_num:
  if guess < 5:
    print(guess, "is too low")
    print("Nope, try again")
    guess = int(input("What's the number?  "))
  elif guess > 5:
    print(guess, "is too high")
    print("Nope, try again")
    guess = int(input("What's the number?  "))
print("Yes! You win!")