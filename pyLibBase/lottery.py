from random import choice

NUM=[0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e']


class Lottery:
    def __init__(self):
        num_list = []
        for _ in range(4):
            num_list.append(choice(NUM))
        self.l_number = num_list

    def get_l_number(self):
        return self.l_number

def get_champion_num():

    champion_num = []
    for _ in range(4):
        champion_num.append(choice(NUM))

    return champion_num


if __name__ == '__main__':
    lottery = Lottery()
    count = 0
    while lottery.l_number != get_champion_num():
        count +=1
        print(f"{lottery.l_number} is not the champion! \nchampion_num = {get_champion_num()}")
        lottery = Lottery()

    print(f"{count} 次后你赢了！\n奖号是{lottery.l_number}")
    # if lottery.l_number == get_champion_num():
    #     print(f"{lottery.l_number} is the champion!")
    # else:
    #     print(f"{lottery.l_number} is not the champion! \nchampion_num = {get_champion_num()}")
