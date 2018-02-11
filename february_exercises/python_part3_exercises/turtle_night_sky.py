import random
from turtle import *

def sky():
  pencolor('white')
  bgcolor("black")
  
  for i in range(200):
      #set pensize bigger for brighter star
      if i % 7 == 0:
        width = 6
      #return pensize to small for most stars, various star size
      else: 
        width = 5
      forward(1)
      right(144)
      up()
      forward(random.randint(1, 80))
      left(random.randint(1, 80))
      down()
      
      

 
if __name__ == "__main__":
    sky() 
    mainloop()