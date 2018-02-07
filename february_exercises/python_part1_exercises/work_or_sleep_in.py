day = int(input("Day of the week (0-6)?  "))
weekdays = [1, 2, 3, 4, 5]
weekend = [0, 6]
if day in weekend:
  print("Sleep in!")
if day in weekdays:
  print("Go to work")
