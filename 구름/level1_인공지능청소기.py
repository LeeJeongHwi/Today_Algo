from sys import stdin

t = int(stdin.readline())

for _ in range(t):
	x,y,n = map(int,stdin.readline().split())
	od = True
	dist = abs(x) + abs(y)
	if dist % 2 == 0: # 짝수 시간인 경우에만 가능
		if n % 2 == 0 and n >= dist:
			print("YES")
		else:
			print("NO")
	else:
		if n % 2 != 0 and n >= dist:
			print("YES")
		else:
			print("NO")
			
# 그냥 단순한 거리계산