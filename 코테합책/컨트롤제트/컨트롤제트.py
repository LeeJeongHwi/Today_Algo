def solution(s):
    st = []
    for cmd in s.split():
        if cmd == "Z":
            st.pop()
        else:
            cmd = int(cmd)
            st.append(cmd)
    return sum(st)