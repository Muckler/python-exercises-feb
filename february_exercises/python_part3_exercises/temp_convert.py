import matplotlib.pyplot as plot
def temp(cels):
  return (cels * (9/5)) + 32
  
day_number = [1, 2, 3, 4, 5]
day_temp = [28, 0, 30, 14, 8]
conv_day = []
for day in day_temp:
  conv_day.append(temp(day))
plot.plot(day_number, conv_day) 
plot.show()


