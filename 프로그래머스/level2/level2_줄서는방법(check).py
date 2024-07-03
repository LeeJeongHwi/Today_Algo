from math import factorial
def solution(n, k):
    # init 
    count = 0
    numlist = [i for i in range(1,n+1)]
    k -= 1
    ans = []
    while n>1:
        fact = factorial(n-1)
        
        index = k // fact
        k = k % fact
        
        n -= 1
        ans.append(numlist.pop(index))
    
    ans.append(numlist.pop())
    return ans
    