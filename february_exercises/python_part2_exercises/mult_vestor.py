my_num = [1, 4, 7]
num2 = [2, 5, 3]
new_num = []
count = 0
for num in my_num:
  new_num.append(num * num2[count])
  count += 1

print(new_num)