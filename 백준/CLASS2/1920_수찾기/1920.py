from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())
list_A = list(map(int,stdin.readline().split()))

list_A.sort()

m = int(stdin.readline())
target = list(map(int,stdin.readline().split()))

def binary_search(num, low, high):
    
    mid = (low+high)//2

    if low > high:
        return False
    
    if list_A[mid] == num:
        return True
    
    elif num > list_A[mid]:
        return binary_search(num, mid+1, high)
    elif num < list_A[mid]:
        return binary_search(num, low, mid-1)

for i in range(m):
    if binary_search(target[i], 0, n-1):
        print(1)
    else:
        print(0)