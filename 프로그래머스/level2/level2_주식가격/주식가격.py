from collections import deque

def solution(prices):

    st = deque()
    ans = []
    limit_t = len(prices)

    for i in range(limit_t):
        for j in range(i+1, limit_t):
            # print(prices[i], prices[j], i, j)
            if prices[i] > prices[j]:
                flag = True
                ans.append(j-i)
                break
        else:
            ans.append(j-i)

    return ans


print(solution([1,2,3,2,3])) # [4,3,1,1,0]
print(solution([1,2,3,2,3,4,5,2])) # [7,6,1,4,3,2,1,0]