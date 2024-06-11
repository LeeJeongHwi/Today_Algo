from sys import stdin
stdin = open('input.txt')
n = int(stdin.readline())

nlist = list(map(int,stdin.readline().split()))
sorted_nlist = sorted(set(nlist))
changed = {sorted_nlist[i]:i for i in range(len(sorted_nlist))}

# for x in nlist:
#     print(changed[x], end=" ")

    # ans += "" ; print(ans) 하는 방식은 O(N^2) 가 소요된다고 본다.
ans = []
for x in nlist:
	ans.append(str(changed[x]))
	
print(" ".join(ans))