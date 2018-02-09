from turtle import *
  
def pent():
  # move into position
  up()
  forward(50)
  left(90)
  forward(50)
  left(90)
  down()
  # draw the pentagon
  forward(100)
  left(72)
  forward(100)
  left(72)
  forward(100)
  left(72)
  forward(100)
  left(72)
  forward(100)

if __name__ == "__main__":
  pent()
  mainloop()

