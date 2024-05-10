from sys import stdin

stdin = open("input.txt")

n = int(stdin.readline())
scores = list(map(int,stdin.readline().split()))

M = max(scores)
new_score = lambda x: x/M * 100
ans = sum(map(new_score,scores))/n
print(ans)

# 그냥 숫자 다 더해서 리스트연산으로 해주면 그만이었음
# sum(scores)/M*100/N