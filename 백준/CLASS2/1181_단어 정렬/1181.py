from sys import stdin
stdin = open('input.txt')
n = int(stdin.readline())
str_list = set([stdin.readline().rstrip() for _ in range(n)])

# 다중 조건은 lambda x : (condition1, condition2, ...)
print("\n".join(sorted(str_list,key=lambda x: (len(x), x))))