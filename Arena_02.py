import Person_02

Person=Person_02

pers1=Person.Person('Первый')
pers2=Person.Person('Второй')
round=0
while pers1.h or pers2.h !=0:
    round+=1
    print(str(round) + ' раунд.')
    print('атакует '+ pers1.name)
    pers2.dam(pers1.damage)
    if pers2.h == 0:
        break
    print('атакует '+ pers2.name)
    pers1.dam(pers2.damage)
    if pers1.h == 0:
        break
