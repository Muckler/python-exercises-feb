from turtle import *
def hex():
  # move into position
  up()
  forward(50)
  left(90)
  forward(50)
  left(90)
  down()
# draw the hexagon
  forward(100)
  left(60)
  forward(100)
  left(60)
  forward(100)
  left(60)
  forward(100)
  left(60)
  forward(100)
  left(60)
  forward(100)

  mainloop()

if __name__ == "__main__":
  hex()