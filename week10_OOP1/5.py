# Create a Vehicle class.
# A Vehicle has
#  make
#  model
#  year
# A Vehicle can do
#  print vehicle type

# Create a constructor method that initializes all instance variables.
# You should write getters and setters for each of the instance variables.
# Instantiate an instance of the class. You may pass any initial values of your choosing.
# Write a method called print vehicle_type, which prints in the form “[year] [make] [model]”
# example. “2021 Toyota Camry”.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_make(self):
        return self.make
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    
    def set_make(self, new_make):
        self.make = new_make
    def set_model(self, new_model):
        self.model = new_model
    def set_year(self, new_year):
        self.year = new_year
    
    # This is the Method
    def vehicle_type(self):
        print(f'{self.make} {self.model} {self.year}')
            
vehicle1 = Vehicle('Toyota', 'Camry', 2021)
vehicle1.vehicle_type() # This enables the Method to initiate