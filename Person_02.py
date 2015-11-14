import random

import Inventar

class Person:
    h=1
    hels=10
    damage=2
    def gan(self):
        pass
    def inv(self):
        pass
    def __init__(self,name):
        self.name=name
    def shoot(self):
        pass
    def dam(self,ur):
        self.hels-=ur
        print("Нанесено урона "+str(ur)+" Здоровья осталось "+ str(self.hels))
        if self.hels<=0:
            self.h=0
            self.dead()
    def dead(self):
        print('Персонаж '+ str(self.name)+' погиб.')




