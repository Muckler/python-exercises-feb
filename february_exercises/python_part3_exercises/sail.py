from turtle import *

def sail_rig():
  
  # draw the sail
  bgcolor('lightblue')
  color("red", "white")
  begin_fill()
  left(90)
  forward(200)
  right(150)
  forward(205)
  right(120)
  forward(105)
  end_fill()

if __name__ == "__main__":
  sail_rig()
  mainloop()