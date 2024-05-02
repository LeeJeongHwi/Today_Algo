from sys import stdin
from collections import deque
stdin = open("input.txt","r")

n = int(stdin.readline())

balloon = deque([(x+1, prior) for x,prior in enumerate(map(int,stdin.readline().split()))])
# using Deque (it seems like PrinterQueue)

x, pr = balloon.popleft()
# Positive Value : popleft() -> append() -> popleft()
# Negative Value : pop() -> appendleft() -> pop()
result = [str(x)]

while balloon:
    for count in range(abs(pr)-1): # 해당 회수만큼 pop,append
        if pr < 0: # Negative Value
            tmp = balloon.pop()
            balloon.appendleft(tmp)
        else:
            tmp = balloon.popleft()
            balloon.append(tmp)
    if pr < 0:
        x, pr = balloon.pop()
        result.append(str(x))
    else:
        x, pr = balloon.popleft()
        result.append(str(x))

print(" ".join(result))

# 해당 문제는 간단한 index 계산으로도 충분히 풀 수 있다.
# pr > 0 일때에는 idx = (idx + tmp) % len(balloon)
# pr < 0 일때에는 idx = (idx + (tmp-1)) % len(balloon)