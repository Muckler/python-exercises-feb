my_num = [2, 8, 3, 5, 2, 7, 8]
new_num = []
#new_num.append(my_num[0])

for num in my_num:
  if num not in new_num:
    new_num.append(num)
  
  
print(new_num)