my_list = [1, 2]
i = 0

nextnum = 0
while nextnum < 4000000:
  j = i +1
  nextnum = my_list[i] + my_list[j]
  my_list.append(nextnum)
  i += 1
print(my_list)
total_sum = 0
for my_num in my_list:
  if my_num % 2 == 0:
    total_sum += my_num
print(total_sum)