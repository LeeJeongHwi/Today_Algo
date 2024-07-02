n = int(input())
stick = [int(input()) for _ in range(n)]
last = stick[-1]
count = 1
for i in range(n-2,-1,-1):
	if stick[i] > last:
		last = stick[i]
		count += 1
print(count)