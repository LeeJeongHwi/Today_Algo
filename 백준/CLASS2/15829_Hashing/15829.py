from sys import stdin

stdin = open("input.txt")

r=31; M=1234567891

alpha = {chr(val): (val-96) for val in range(97,123)}

L = int(stdin.readline())
line = stdin.readline().rstrip()

ans = 0
for i,char in enumerate(line):
    ans += alpha[char] * (r**i)

print(ans%M)

# ord("a") = 97을 반환, Char를 int로 바꿔주는 것...