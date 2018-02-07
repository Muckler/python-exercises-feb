my_num = [1, 4, 32, 7, 18, 5]
smallest = 100000
for num in my_num:
  if num < smallest:
    smallest = num
  elif num > smallest:
    smallest = smallest
print(smallest)