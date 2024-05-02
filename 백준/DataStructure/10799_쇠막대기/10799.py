from sys import stdin

stdin = open("input.txt","r")

stick = stdin.readline().rstrip()

size = 0
result = 0
for i in range(len(stick)):
    if stick[i] == "(":
        size+=1
        continue

    if stick[i] == ")":
        if stick[i-1] == "(":
            size-=1
            result+=size
        else:
            size-=1
            result+=1

print(result)
