'''
	[문제]
	    100 ~ 300 사이의 숫자 중에서 
     	[조건1] 8의 배수를 출력하고, 
      	[조건2] 그 총합을 구하시오.
		[조건3] 개수를 구하시오.
	[정답]
		104 112 120 128 136 144 152 160 168 176 184 192 200 208 216 224 232 240 248 256 264 272 280 288 296 
		total = 5000
		count = 25
'''

print('===[2023-01-21 (목) #01]===')

num = 8
total = 0
count = 0

i = 100
while i <= 300:
	if i % num == 0:
		print(i, end = " ")
		total += i
		count += 1
	i += 1

print()
print("total =", total)
print("count =", count)