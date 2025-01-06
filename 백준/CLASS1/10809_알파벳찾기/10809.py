from sys import stdin
stdin = open('input.txt')

strs = stdin.readline().rstrip()
# 97 ~ 122
alphas = ["-1" for _ in range(97,123)]

for i, ch in enumerate(strs):
    index = ord(ch)-96 - 1
    if alphas[index] == "-1":
        alphas[index] = f"{i}"

print(" ".join(alphas))