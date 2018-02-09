from turtle import *
def runtri():

  # move into position
  up()
  forward(50)
  left(90)
  forward(50)
  left(90)
  down()
  # draw the triangle
  pencolor('blue')
  forward(100)
  left(120)
  forward(100)
  left(120)
  forward(100)

  
if __name__ == "__main__":
    runtri() 
    mainloop()