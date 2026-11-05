from car import ElectricCar

my_leaf = ElectricCar("audi", "a4", 2016)
print(my_leaf.get_descriptive_name())
my_leaf.batter.describe_battery()
my_leaf.batter.get_range()