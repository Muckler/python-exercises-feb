from turtle import *

def boat_rig():
  
  up()
  left(90)
  forward(20)
  down()
  color("darkblue", '#552600')
  begin_fill()
  right(90)
  forward(300)
  left(130)
  forward(95)
  left(49)
  forward(400)
  left(91)
  forward(78)
  left(90)
  forward(300)
  end_fill()
  mainloop()
  

if __name__ == "__main__": 
  boat_rig()
  mainloop()