from sys import stdin
import datetime
stdin = open('input.txt')

H, M = map(int,stdin.readline().split())

if M >= 45:
    M-=45
else:
    M = 60-abs(M-45)
    if H >= 1:
        H -= 1
    else:
        H = 23

print(H, M)