from sys import stdin
from collections import deque
stdin = open('input.txt')
n = int(stdin.readline())
def dslr(A,B):
    visit = [[] for _ in range(10001)]
    q = deque()

    visit[A] = [A, ""]
    q.append(A)
    while q:
        now = q.popleft()
        if now == B:
            ans=""
            nows = visit[now]
            while True:
                if nows[1] == "":
                    return ans
                ans = nows[1] + ans
                nows = visit[nows[0]]
                        
        for cmd in ["D","S","L","R"]:

            if cmd == "D":
                num = now*2 if now*2 <= 9999 else now*2 % 10000
                if not visit[num]:
                    visit[num] = [now, "D"]
                    q.append(num)

            elif cmd == "S":
                num = now-1 if now-1 >= 0 else 9999
                if not visit[num]:
                    visit[num] = [now, "S"]
                    q.append(num)    

            elif cmd == "L":
                rotate_num = (now%1000)*10 + (now//1000)
                if not visit[rotate_num]:
                    visit[rotate_num] = [now, "L"]
                    q.append(rotate_num)

            elif cmd == "R":
                rotate_num = (now%10)*1000 + (now//10)
                if not visit[rotate_num]:
                    visit[rotate_num] = [now, "R"]
                    q.append(rotate_num)


for _ in range(n):
    A, B = map(int,stdin.readline().split())
    print(dslr(A,B))