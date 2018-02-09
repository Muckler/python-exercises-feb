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
  pencolor('orange')
  forward(100)
  left(90)
  forward(100)
  left(90)
  forward(100)
  left(90)
  forward(100)
  
if __name__ == "__main__":
    square()
    mainloop()