'''
[문제] 
    1~30 사이의 숫자를 출력한다.
    
[옆으로 출력]
    위와 같이 반복문을 출력하면 세로로 길게 출력되어서 보기가 힘들다.
    그래서 옆으로 출력하는 방법을 제공한다.  
    아래와 같이 표현하면 줄 바꿈이 삭제되어 옆으로 출력된다.         
    print(변수)  ==> print(변수, end=" ")
'''

print('===[2023-01-19(목) #01]===')

i = 1
while i <= 30:
    print(i, end = " ")
    i += 1

    

# print('===[정답풀이]===')
# i = 1

# while i <= 30:
#     print(i, end=" ")
#     i += 1

# print()
# print("Hello, Python!")




