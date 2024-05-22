from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())

# Greedy

max_q = n//5

cnts = []

for q in range(max_q,-1,-1): # q = 5kg 개수
    
    rem_5 = n-(q*5)

    if rem_5 == 0:
        cnts.append(q)
        break
    elif rem_5 < 0:
        continue
    
    cnt_3 = rem_5//3
    rem_3 = rem_5%3

    if rem_3 != 0:
        continue
    elif rem_3 == 0:
        cnts.append(cnt_3 + q)

if cnts:
    print(min(cnts))
else:
    print(-1)