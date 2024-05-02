from sys import stdin

stdin = open("input.txt","r")

N = int(stdin.readline())

def solution(x,r):
    return

xr = []
for _ in range(N):
    x, r = map(int,stdin.readline().split())
    xr.append([x,r])
    
print(xr)
