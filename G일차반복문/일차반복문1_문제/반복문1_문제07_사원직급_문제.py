'''
    [문제] 아래 조건을 만족하는 식을 작성하시오.  
        [조건1] 사원 번호가 1~30까지 있다.
        [조건2] 1~5번은 과장
        [조건3] 6번에서 15는 대리
        [조건4] 16번에서 30번은 사원이다. 
        각각의 번호를 출력하면서 알아볼 수 있게 각 명칭을 같이 출력하시오.   
    [정답]
        1 과장
        2 과장
        ...
        ...
        ...
        6 대리
        ...
        ...
        ...
        16 사원
        ...
        ...
        ...
'''

print('===[2023-03-03(금)]===')

i = 1
while i <= 30:
    if i <= 5:
        print(i, "과장")
    elif i <= 15:
        print(i, "대리")
    else:
        print(i, "사원")
    i += 1








# print('===[2023-01-19(목) #01]===')

# i = 1
# while i <= 30:
#     if i <= 5:
#         print(i, "과장")
#     elif i <= 15:
#         print(i, "대리")
#     else:
#         print(i, "사원")
#     i += 1