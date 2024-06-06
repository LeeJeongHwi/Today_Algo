from sys import stdin
stdin = open("input.txt","r")

inps = stdin.readline().rstrip()

split_number = inps.split("-")

type_int = []
for spnum in split_number:
    # if 1. "00009" -> int
    int_num = 0
    split_plus = spnum.split("+")
    for sp in split_plus:
        int_num+=int(sp)
    type_int.append(int_num)
    
ans = type_int[0]
for i, ti in enumerate(type_int):
    if i==0:
        continue
    ans -= ti

print(ans)
    

