from random import randint
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        return randint(1,self.sides)


def get_die_x(x):

    die_list = []
    for _ in  range(10):
        die = Die(x)
        die_list.append(die.roll_dice())
    return die_list


print(get_die_x(10))
print(get_die_x(20))

