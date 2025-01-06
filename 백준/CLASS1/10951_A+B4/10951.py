from sys import stdin
stdin = open('input.txt')

while True:
    try:
        a,b = map(int,stdin.readline().split())
        print(a+b)
    except:
        break
