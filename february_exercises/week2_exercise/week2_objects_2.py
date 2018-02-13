class Vehicle: 
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
  def print_info (self):
    print(year, make, model)

car = Vehicle('Nissan', 'Leaf', 2015)
print(car.make, car.model, car.year)