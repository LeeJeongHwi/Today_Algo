n = int(input())

for _ in range(n):
	strs = input()
	mo = []
	for s in strs:
		if s in ["a","e","i","o","u","A","E","I","O","U"]:
			mo.append(s)
	if mo:
		print("".join(mo))
	else:
		print("???")