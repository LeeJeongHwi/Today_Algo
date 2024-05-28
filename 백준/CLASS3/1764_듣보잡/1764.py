from sys import stdin
stdin = open('input.txt')

n, m = map(int,stdin.readline().split())

n_dict = {}
count = 0
for _ in range(n):
    name = stdin.readline().rstrip()
    if name not in n_dict:
        n_dict[name] = 1
    else:
        n_dict[name] += 1

ans = []
for _ in range(m):
    name = stdin.readline().rstrip()
    try:
        n_dict[name] += 1
    except KeyError:
        continue
    count+=1
    ans.append(name)

print(count)
ans.sort()
print("\n".join(ans))