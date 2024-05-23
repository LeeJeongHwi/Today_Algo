from sys import stdin
from collections import deque
stdin = open('input.txt')

ch_dict = {")":"(", "]":"["}

def check_Line(line):
    st = deque()
    for ch in line:
        if ch == "(" or ch == "[":
            st.append(ch)
        elif ch == ")" or ch=="]":
            if not st:
                return False
            top = st.pop()
            if top != ch_dict[ch]:
                return False
    if st:
        return False
    return True

while True:
    line = stdin.readline().rstrip()
    if line == ".":
        break
    if check_Line(line):
        print("yes")
    else:
        print("no")