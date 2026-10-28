from car import Car

class Battery:
    def __init__(self, battery_size=40) :
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"{self.battery_size} battery")

    def get_range(self):
        e_range = 0
        if self.battery_size == 40:
            e_range = 150
        else:
            e_range = 225

        print(f"This car can go about {e_range} miles on a full charge.")

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.batter = Battery()
