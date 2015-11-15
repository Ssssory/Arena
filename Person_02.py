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
    def miss(self):
        x=random.randint(0,100)
        missbar=[0,2,4,6,8,9]
        if x in missbar:
            miss= True
        else:
            miss= False
        return miss
    def dam(self,ur):
        x=self.miss()
        if not(x):
            self.hels-=ur
            print("Нанесено урона "+str(ur)+" Здоровья осталось "+ str(self.hels))
            if self.hels<=0:
                self.h=0
                self.dead()
        else:
            print('__Промах!___')
    def dead(self):
        print('Персонаж '+ str(self.name)+' погиб.')
    def __str__(self):
        st=str(self.name)+' оружие: '+str(self.weapon)+ ' здоров:'+ str(self.hels)
        return st




