from sys import stdin

stdin = open("input.txt","r")
n = int(stdin.readline())

for _ in range(n):
    stack = []    
    line = stdin.readline()
    flag = True
    for ps in line:
        if ps == "(":
            stack.append(ps)
            continue
        elif ps == ")":
            
            if stack:
                stack.pop()

            else:
                flag = False
                break
    
    if stack or (not flag):
        print("NO")
    
    else:
        print("YES")