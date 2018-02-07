my_num = [1, 4, 32, 7, 18, 5]
biggest = 0
for num in my_num:
  if num > biggest:
    biggest = num
  elif num < biggest:
    biggest = biggest
print(biggest)