from sys import stdin
stdin = open('input.txt')
n, m = map(int,stdin.readline().split())

tree_num = list(map(int,stdin.readline().split()))

# 중간 크기의 높이에서 자르고나서, 그 합계보고 합계가 낮으면 더 낮게 잘라야되고, 합계가 높으면 더 높게 잘라야한다

def binary_search():
    high = max(tree_num)
    low = 1 # 입력 기준 값이 1 이기 때문
    while True:
        if low > high:
            return high
        
        mid = (low + high) // 2
        cutting = list(map(lambda x: x-mid if x>mid else 0, tree_num))
        cut_sum = sum(cutting)

        # 쭉 봐야하는 이유가, 최댓값을 찾기 위함. 그리고 딱 맞지 않을때도 있음

        if cut_sum < m:
            high = mid-1
        elif cut_sum >= m:
            low = mid+1
    

print(binary_search())
