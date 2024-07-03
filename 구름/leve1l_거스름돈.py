# Greedy
money = int(input())
count = 0
# 40개 먼저 다 처리
for coin in [40,20,10,5,1]:
	count += money // coin
	money = money % coin
	if money == 0:
		break
print(count)
