size = int(input('How big is the square?  '))
my_list = []
for each in range(1, size + 1):
  my_list.append(("*") * size)

for star in my_list:
  print(star)