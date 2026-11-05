from car import Car
from electric_car import ElectricCar as Ec

my_mustang = Car("mustang", "Mustang", 2016)
print(my_mustang.get_descriptive_name())
my_leaf = Ec("nissan", "Leaf", 2016)

print(my_leaf.get_descriptive_name())