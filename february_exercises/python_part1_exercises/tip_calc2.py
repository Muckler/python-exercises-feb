total_bill = int(input("What is total bill?  "))
service = input("Level of service?  ")
split = int(input("Split how many ways?  "))

if service == "good":
  tip = total_bill * .20
  tip_total = total_bill + tip
  ea_person = tip_total / split
  print("Tip amount: $", tip)
  print("Total amount: $", tip_total)
  print("Amount per person: $", ea_person)

elif service == "fair":
  tip = total_bill * .15
  tip_total = total_bill + tip
  ea_person = tip_total / split
  print("Tip amount: $", tip)
  print("Total amount: $", tip_total)
  print("Amount per person: $", ea_person)

elif service == "bad":
  tip = total_bill * .15
  tip_total = total_bill + tip
  ea_person = tip_total / split
  print("Tip amount: $", tip)
  print("Total amount: $", tip_total)
  print("Amount per person: $", ea_person)
