from sys import stdin
stdin = open('input.txt')
n = int(stdin.readline())
m = int(stdin.readline())

S = stdin.readline().rstrip()

ioi = "IO" * n + "I"
ioi_len = (2*n)+1

# ==== Score 50 ==== # 

def score50():
    cnt = 0
    for i in range(m-(2*n)):
        if S[i:2*n+1+i] == ioi: #여기서 시간이 걸릴 것으로 생각
            cnt += 1
    print(cnt)

# O(N)으로 끝내야함
def score100():
    i = cnt = ans = 0
    while i < m-1:
        if S[i:i+3] == "IOI":
            cnt +=1
            i += 2
            if cnt == n:
                cnt -= 1
                ans += 1
        else:
            i += 1
            cnt = 0
    print(ans)

score100()