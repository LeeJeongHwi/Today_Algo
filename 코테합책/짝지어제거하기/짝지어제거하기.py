def solution(s):
    st = []
    for ch in s:
        if not st:
            st.append(ch)
            continue
        if st[-1] == ch:
            st.pop()
        else:
            st.append(ch)
            
    if st:
        return 0
    else:
        return 1

    return answer