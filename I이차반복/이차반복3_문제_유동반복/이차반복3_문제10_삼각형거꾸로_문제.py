'''
	[문제]
		아래와 같이 삼각형을 출력하시오.	
	[예시]
		7
		6 7
		5 6 7
		4 5 6 7
		3 4 5 6 7
		2 3 4 5 6 7
		1 2 3 4 5 6 7
'''

print('===[2023-02-02 (목)]===')

for i in range(7):
	i += 1
	num = - i + 8
	for j in range(i):
		print(num, end = " ")
		num += 1
	print()