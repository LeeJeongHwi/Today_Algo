from sys import stdin
stdin = open('input.txt')

mods = set()

for i in range(10):
    n = int(stdin.readline())
    mods.add(n%42)
print(len(mods))