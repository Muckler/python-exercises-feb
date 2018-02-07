import random

secret_num = random.randint(1, 10)
print("I am thinking of a number between 1 and 10")
guess = int(input("What's the number?  "))
count_guess = 1
while guess != secret_num and count_guess < 2:
  if guess < secret_num:
    print(guess, "is too low")
    print("Nope, try again")
    guess = int(input("What's the number?  "))
    count_guess += 1
  elif guess > secret_num:
    print(guess, "is too high")
    print("Nope, try again")
    guess = int(input("What's the number?  "))
    count_guess += 1
if guess == secret_num:
  print("Yes! You win!")
else:
  print("Wait, you ran out of guesses!")
