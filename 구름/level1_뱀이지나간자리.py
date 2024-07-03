from sys import stdin
N,M = map(int,stdin.readline().split())

right_left = True # True : right

for i in range(1,N+1):
	if i % 2 != 0:
		print("#"*M)
	else:
		if right_left:
			print("."*(M-1)+"#")
		else:
			print("#"+"."*(M-1))
		right_left = not right_left
			