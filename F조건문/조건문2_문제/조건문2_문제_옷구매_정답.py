'''
	[문제] 
		철수는 상점에서 24600원짜리 옷을 구매했다.
		500원짜리 동전으로만 옷값을 낸다면,
		동전이 몇 개 필요한지 구하시오.
	[정답]
		50
'''

옷가격 = 24600

동전개수 = 옷가격 // 500
if 옷가격 % 500 != 0:
	동전개수 = 동전개수 + 1
print(동전개수)