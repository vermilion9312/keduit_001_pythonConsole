'''
	[문제] 
		사탕 62개와 초콜릿 88개를 각각 남김없이 똑같이 최대한 
		많은 학생에게 나눠주려고 할 때,  학생 수를 구하시오.
		단, 사탕은 2개가 남고 초콜릿은 4개가 남는다.
	[정답]
		12
'''

print("===[2023-10-27 (금)]===")

CANDY = 62
CHOCHOLATE = 88

student = 1

while student <= CANDY:
    
	if CANDY % student == 2 and CHOCHOLATE % student == 4:
		quotient = student

	student += 1

print(quotient)