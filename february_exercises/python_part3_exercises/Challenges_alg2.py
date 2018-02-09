my_list = []
for i in range(1, 1000):
  if i % 3 == 0 or i % 5 == 0:
    my_list.append(i)
total_sum = 0
for j in my_list:
  total_sum += j

print(total_sum)
    