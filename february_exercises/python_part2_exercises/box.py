width = int(input('Width?  '))
height = int(input('Height?  '))
box = []
box.insert(0, "* " * width)
for each in range(0, height - 2):
  box.insert(1, "* " + (" " * (width)) + " *")
box.append("* " * width)
for star in box:
  print(star)

  
 