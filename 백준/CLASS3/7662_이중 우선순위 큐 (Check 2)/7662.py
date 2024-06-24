from sys import stdin
import heapq

# Min-Max Heap 구현 --> 꼭 다시 구현해볼것... Notion에다가도 후기 쓰기
stdin = open('input.txt')
T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    maxh = []
    minh = []
    visit = {}
    for _ in range(N):
        cmd, num = stdin.readline().split()
        
        if cmd == "I":
            num = int(num)
            heapq.heappush(minh, num)
            heapq.heappush(maxh, -num)

            if num in visit:
                visit[num] += 1
            else:
                visit[num] = 1
            
        
        elif cmd == "D":
            if num == "1":
                while maxh and visit[-maxh[0]] == 0:
                    heapq.heappop(maxh)
                if maxh:
                    popn = heapq.heappop(maxh)
                    if visit[-popn] > 0:
                        visit[-popn] -= 1
                    


            elif num == "-1":
                # 동기화
                while minh and visit[minh[0]] == 0:
                        heapq.heappop(minh)
                if minh:
                    popn = heapq.heappop(minh)
                    if visit[popn] > 0:
                        visit[popn] -= 1
                    
    while minh and visit[minh[0]] == 0:
        heapq.heappop(minh)
    while maxh and visit[-maxh[0]] == 0:
        heapq.heappop(maxh)
    
    if not minh and not maxh:
        print("EMPTY")
    else:
        print(-maxh[0], minh[0])
    
            