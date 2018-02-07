height = int(input("Triangle height?  "))
tri = []
for i in range(1, height + 1):
  tri.append("* " * i)
  
j = int(height)
for star in tri:
  print((" " * j), star)
  j = j - 1
    

