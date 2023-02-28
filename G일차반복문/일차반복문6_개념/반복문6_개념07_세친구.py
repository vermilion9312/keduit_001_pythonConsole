'''
[문제] 
	자전거로 운동장을 한 바퀴 도는데 
	철수는 90초, 
	영희는 60초, 
	민수는 45초가 걸린다.
	이와 같은 속력으로 같은 곳에서 동시에 출발하여 같은 방향으로 운동장을 돌 때, 
	1) 세 사람이 처음으로 출발점에서 다시 만나게 되는 것은 몇초 후인지 구하시오.
	2) 다시 만나게 되었을 때 민수는 몇 바퀴 돌았을 때인지 구하시오.
[정답]
	1) 180초
	2) 4바퀴
'''
철수 = 90
영희 = 60
민수 = 45

총시간 = 0

i = 45
run = 1
while run == 1:
	if i % 철수 == 0 and i % 영희 == 0 and i % 민수 == 0:
		총시간 = i
		run = 0
	i += 1
print(총시간)

민수_바퀴수 = 총시간 // 민수
print(민수_바퀴수)
