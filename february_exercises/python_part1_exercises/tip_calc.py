total_bill = int(input("What was your total bill?"))
service = input("Was your service good, fair, or bad?")
if service == "good":
  tip = total_bill * .20
  print("Your tip is", tip)
  print("Your total amount is:", total + tip)
elif service == "fair":
  tip = total_bill * .15
  print("Your tip is", tip)
  print("Your total amount is:", total_bill + tip)
elif service == "bad":
    tip = total_bill * .10
    print("Your tip is", tip)
    print("Your total amount is:", total_bill + tip)

    pass