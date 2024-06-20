from sys import stdin
from collections import deque
stdin = open('input.txt')

T = int(stdin.readline())
    
def AC_lang():
    func = stdin.readline().rstrip()
    arr_N = int(stdin.readline())
    arr = deque(eval(stdin.readline().rstrip()))
    rev = False

    for f in func:
        if f == "R":
            rev = not rev
            continue
        
        if arr:
            if rev: # Reversed
                arr.pop()
            else: # Not Reversed
                arr.popleft()
            arr_N -= 1
        else:
            print("error")
            return
    if not rev:
        print("["+",".join(map(str,arr))+"]")
    if rev:
        print("["+",".join(map(str,reversed(arr)))+"]")

for _ in range(T):
    AC_lang()

# Deque를 안쓰고 start,end 로 만들어서 reverse일때 end+1, 아닐때 start+1로 처리하면
# 시간이 단축