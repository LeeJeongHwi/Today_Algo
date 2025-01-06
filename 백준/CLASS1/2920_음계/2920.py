from sys import stdin
stdin = open('input.txt')

nlist = list(map(int,stdin.readline().split()))

# inits
flag = ""
if nlist[1] > nlist[0]:
    flag = "ascending"
elif nlist[1] < nlist[0]:
    flag = "descending"

for i in range(1,8):
    if flag == "ascending":
        if nlist[i] > nlist[i-1]:
            continue
        else:
            flag = "mixed"
    elif flag == "descending":
        if nlist[i] < nlist[i-1]:
            continue
        else:
            flag = "mixed"
    else:
        break
print(flag)