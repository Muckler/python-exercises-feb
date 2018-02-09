from turtle import *
def octa():

  # move into position
  up()
  forward(100)
  left(90)
  forward(50)
  left(90)
  down()
  # draw the hexagon
  pencolor('yellow')
  forward(150)
  left(45)
  forward(150)
  left(45)
  forward(150)
  left(45)
  forward(150)
  left(45)
  forward(150)
  left(45)
  forward(150)
  left(45)
  forward(150)
  left(45)
  forward(150)
if __name__ == "__main__":
  octa()
  mainloop()