'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		1
		1 2
		1 2 3
		1 2 3 1
		1 2 3 1 2
		1 2 3 1 2 3
		1 2 3 1 2 3 1
		1 2 3 1 2 3 1 2
		1 2 3 1 2 3 1 2 3
		1 2 3 1 2 3 1 2 3 1
'''

print('===[2023-01-31 (화)]===')

for i in range(10):
	val = 1
	for j in range(i + 1):
		print(val, end = " ")
		val += 1
		if val == 4:
			val = 1
	print()