from myexception.exceptions import AgeException


def calculate_something(age):
    if age < 0 or age > 100:
        raise AgeException("Age must be between 0 and 100")


try:
    calculate_something(-1)
except AgeException as e:
    print(e)

class Celsius:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

human = Celsius(37)
# human.temperature = 37
print(human.temperature)
print(human.to_fahrenheit())

class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

human = Celsius()
human.set_temperature(37)
print(human.get_temperature())
print(human.to_fahrenheit())



class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

human = Celsius()
human.temperature = 37
print(human.temperature)
print(human.to_fahrenheit())


