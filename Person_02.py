import random

import Inventar
items=Inventar.items()

class Person:
    h=1
    hels=10
    damage=2
    def gun(self):
        x=random.randint(0,2)
        gunlist=['пистолет','автомат','пулемёт']
        sel=gunlist[x]
        self.damage=Inventar.items.igun(self,sel)
        self.weapon=sel
    def inv(self):
        pass
    def __init__(self,name):
        self.name=name
        self.gun()
    def shoot(self):        
        x=random.randint(0,len(self.damage)-1)
        ur=self.damage[x]
        return ur
    def dam(self,ur):
        self.hels-=ur
        print("Нанесено урона "+str(ur)+" Здоровья осталось "+ str(self.hels))
        if self.hels<=0:
            self.h=0
            self.dead()
    def dead(self):
        print('Персонаж '+ str(self.name)+' погиб.')




