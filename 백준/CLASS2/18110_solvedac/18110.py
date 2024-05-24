from sys import stdin
stdin = open('input.txt')

# Round 함수 사용시 무조건 에러남
def roundUp(num):
    if (num- int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

def solve():
    n = int(stdin.readline())
    if n == 0:
        print(0)
        return
    trim = roundUp(n * 0.15)

    scs = [int(stdin.readline()) for _ in range(n)]
    scs.sort()
    trim_data = scs[trim:n-trim]
    print(roundUp(sum(trim_data)/len(trim_data)))

solve()