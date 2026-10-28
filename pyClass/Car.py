class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return f"The car make: {self.make} model: {self.model} year: {self.year}"

    def read_odometer(self):
        """
        打印一条指出汽车行驶里程的消息
        """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, mileage):
        self.odometer_reading += mileage


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has {self.battery_size}kWh battery.")

    def get_range(self):
        e_range = 0
        if self.battery_size == 40:
            e_range = 150
        elif self.battery_size == 65:
            e_range = 225
        print(f"this car can go about {e_range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
            print("This car is not pro battery, but upgrade is now 65kWh.")

        else:
            print("This battery is pro!")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print(f"This car has a {self.battery.battery_size} kWh battery.")


if __name__ == '__main__':
    my_leaf = ElectricCar('Tesla', 'Tesla', 2019)
    my_leaf.describe_battery()
    my_leaf.battery.upgrade_battery()
    my_leaf.describe_battery()
