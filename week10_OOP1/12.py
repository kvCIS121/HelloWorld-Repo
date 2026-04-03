# Create a TemperatureInCelsius class.
# A TemperatureInCelsius has
#  temp_value

# A TemperatureInCelsius can do
#  to_fahrenheit

# Clarification: temp value is the temperature in Celsius.
# Create a constructor method that initializes all instance variables.
# You should write getters and setters for each of the instance variables.
# Instantiate an instance of the class. You may pass any initial values of your choosing.\
# The to_fahrenheit() method should return the temperature in Fahrenheit calculated as:
# Fahrenheit = (Celsius * 9/5) + 32.


class TemperatureInCelsius:
    def __init__(self, temp_value):
        self.temp_value = temp_value
    
    def get_temp_value(self):
        return self.temp_value
    
    def set_temp_value(self, new_temp_value):
        self.temp_value = new_temp_value
    
    def to_fahrenheit(self):
        celsius = self.temp_value
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

temp1 = TemperatureInCelsius(7)
temp1.to_fahrenheit()
print(temp1.to_fahrenheit())
