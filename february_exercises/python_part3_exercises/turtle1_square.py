from turtle import *
# move into position
def square():
  up()
  forward(50)
  left(90)
  forward(50)
  left(90)
  down()
  # draw the square
  forward(100)
  left(90)
  forward(100)
  left(90)
  forward(100)
  left(90)
  forward(100)
  mainloop()
if __name__ == "__main__":
    square()