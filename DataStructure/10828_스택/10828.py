from sys import stdin

stdin = open("input.txt","r")
n = int(stdin.readline())

stack = []

def push(x):
    global stack
    stack.append(x)

def pop():
    global stack
    if stack:
        return stack.pop()
    else:
        return -1

def size():
    global stack
    return len(stack)

def empty():
    global stack
    if stack:
        return 0
    else:
        return 1

def top():
    global stack
    if stack:
        return stack[-1]
    else:
        return -1

def exec(n):
    for _ in range(n):
        line = stdin.readline()
        op = line.split()
        if op[0] == "push":
            push(op[1])
        else:
            if op[0] == "pop":
                print(pop())
            elif op[0] == "size":
                print(size())
            elif op[0] == "empty":
                print(empty())
            elif op[0] == "top":
                print(top())
exec(n)
