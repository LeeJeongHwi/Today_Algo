from sys import stdin
stdin = open('input.txt')

n, k = map(int,stdin.readline().split())


coins = []

for _ in range(n):
    coin = int(stdin.readline())
    
    if coin <= k:
        coins.append(coin)

coins.sort(key=lambda x:-x)

count = 0
rem = k
for i in range(len(coins)):
    count += rem // coins[i]
    rem = rem % coins[i]
    if rem == 0:
        break
print(count)