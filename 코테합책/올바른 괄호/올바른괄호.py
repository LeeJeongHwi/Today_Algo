def solution(s):
    st = []
    for br in s:
        if br == "(":
            st.append(br)
        else:
            if not st:
                return False
            else:
                st.pop()
    if st:
        return False
    return True