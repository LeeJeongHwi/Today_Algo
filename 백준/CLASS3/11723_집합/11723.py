from sys import stdin
stdin = open('input.txt')

m = int(stdin.readline())

sets = set()

for _ in range(m):
    functions = stdin.readline().split()

    if functions[0] == "add":
        sets.add(int(functions[1]))
    elif functions[0] == "remove":
        if int(functions[1]) in sets:
            sets.remove(int(functions[1]))
    elif functions[0] == "check":
        if int(functions[1]) in sets:
            print(1)
        else:
            print(0)
    elif functions[0] == "toggle":
        if int(functions[1]) in sets:
            sets.remove(int(functions[1]))
        else:
            sets.add(int(functions[1]))
    elif functions[0] == "all":
        sets = {x for x in range(1,21)}
    elif functions[0] == "empty":
        sets = set()