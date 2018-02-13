import json
import matplotlib.pyplot as plot

with open('week2_json_data.json', 'r') as fh:
  my_data = json.load(fh)
  print(my_data)
#taking data that is dictionary and converting values in the key 'data' to a list of those values
data_graph = my_data.get('data')
print(data_graph)
#single line to unpack the data with 'zip' and '*' from pairs in data_graph to x and y so that it may be plotted
x, y = zip(*data_graph)
plot.plot(x, y)
plot.show()
