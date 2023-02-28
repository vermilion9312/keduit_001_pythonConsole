'''
    [문제]
        철수는 게임을 하고 있다. 
        monster는 게임의 적 4마리를 의미하고 
        숫자는 몬스터의 체력을 의미한다.
        
        철수의 공격력은 5이다.    
        총 다섯번을 반복하면서 
        랜덤으로 몬스터 중 하나를 선택해서 공격한다.
        모든 몬스터들을 공격한 후 몬스터들의 체력을 출력하시오.
        단, 몬스터 체력은 0이 되면 더 이상 내려가지 않는다.
    [예시]
        1 번째 몬스터 공격! : [9, 2, 8, 6]
        0 번째 몬스터 공격! : [4, 2, 8, 6]
        3 번째 몬스터 공격! : [4, 2, 8, 1]
        2 번째 몬스터 공격! : [4, 2, 3, 1]
        1 번째 몬스터 공격! : [4, 0, 3, 1]
'''
import random

monster = [9, 7, 8, 6]
power = 5

count = 0
while True:
    r = random.randint(0, len(monster) - 1)

    if monster[r] > 0:
        if monster[r] - power < 0:
            monster[r] = 0
        else:
            monster[r] -= power
        print(r, "번째 몬스터 공격! :", monster)
        count += 1
    
    if count == 5:
        break

    


