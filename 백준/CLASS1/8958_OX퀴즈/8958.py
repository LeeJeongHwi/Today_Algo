from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())

def calc(corrects):
    ans = 0
    counts = 0
    for i, ox in enumerate(corrects):
        if ox == "O":
            counts += 1
        else:
            counts = 0
        ans+=counts

    return ans

for _ in range(n):
    corrects = stdin.readline().rstrip()
    print(calc(corrects))