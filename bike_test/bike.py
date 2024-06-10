class Bike:
    def __init__(self):
        self.isOn = False
        self.acceleration = 0
        self.gear = 1

    def turn_on(self):
        self.isOn = True

    def turn_off(self):
        self.isOn = False

    def is_on(self):
        return self.isOn

    def set_acceleration(self, acceleration):
        self.acceleration = acceleration
        self.gear_speed()

    def get_acceleration(self):
        return self.acceleration

    def increase_by_gear(self):
        if self.isOn and self.acceleration >= 0:
            self.acceleration += self.gear
        self.gear_speed()

    def set_gear(self, gear):
        if self.isOn and 1 <= gear <= 4:
            self.gear = gear

    def get_gear(self):
        return self.gear

    def decrease_by_gear(self):
        if self.isOn and self.acceleration >= 0:
            self.acceleration -= self.gear
        self.gear_speed()

    def gear_speed(self):
        if 0 <= self.acceleration <= 20:
            self.gear = 1
        elif 21 <= self.acceleration <= 30:
            self.gear = 2
        elif 31 <= self.acceleration <= 40:
            self.gear = 3
        elif self.acceleration >= 41:
            self.gear = 4
