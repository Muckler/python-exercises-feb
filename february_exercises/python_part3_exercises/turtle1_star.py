from turtle import *

def star():
  color("red", "green")
  begin_fill()
  up()
  left(40)
  forward(80)
  down()
  
  
  for i in range(5):
      forward(100)
      right(144)
  end_fill()
if __name__ == "__main__":
    star()
    mainloop()