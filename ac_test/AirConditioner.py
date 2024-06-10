class AirConditioner:
    def __init__(self):
        self.isOn = False
        self.temperature = 0

    def turn_on(self):
        self.isOn = True

    def turn_off(self):
        self.isOn = False

    def is_on(self):
        return self.isOn

    def set_temperature(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def increase_temperature(self) :
        if self.is_on() and self.temperature < 30:
            self.temperature +=1

    def decrease_temperature(self):
        if self.isOn and self.temperature > 16:
            self.temperature -= 1

