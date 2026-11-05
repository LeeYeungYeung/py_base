class Employee:

    def __init__(self, last_name, first_name, annul=0):
        self.last_name = last_name
        self.first_name = first_name
        self.annul = annul

    def give_raise(self,mon = 5000):
        self.annul += mon
