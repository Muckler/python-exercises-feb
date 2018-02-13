import json
import matplotlib.pyplot as plot


with open('week2_json_data.json', 'r') as fh:
  my_data = json.load(fh)
  print(my_data)

plot.plot(my_data)