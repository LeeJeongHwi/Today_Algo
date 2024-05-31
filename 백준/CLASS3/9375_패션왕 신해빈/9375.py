from sys import stdin
stdin = open('input.txt')
n = int(stdin.readline())

def solve(num):
    wearSet = {}
    for _ in range(num):
        _, w_type = stdin.readline().split()
        if w_type not in wearSet:
            wearSet[w_type] = 1
        else:
            wearSet[w_type] += 1

    values = wearSet.values()
    
    count = 1
    for c in values:
        count *= (c+1)
    
    print(count-1)




for _ in range(n):
    num = int(stdin.readline())
    if num == 0:
        print(0)
        continue
    solve(num)