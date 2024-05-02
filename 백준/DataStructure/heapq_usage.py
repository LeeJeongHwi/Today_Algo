# priority Queue를 구현할 때 쓴다

import heapq

# 기본적으로 heapq는 최소힙으로 구현되어있음

hq = []

heapq.heappush(hq,50)
heapq.heappush(hq,10)
heapq.heappush(hq,20)

print(hq)

hq2 = [50 ,10, 20]
heapq.heapify(hq2)

print(hq2)

# heappop

result = heapq.heappop(hq)

# 최대 힙
heap_items = [1,3,5,7,9]

max_heap = []
for item in heap_items:
  # 0번째원소는 인덱스, 1번째 원소가 실제값
  heapq.heappush(max_heap, (-item, item))

print(max_heap)