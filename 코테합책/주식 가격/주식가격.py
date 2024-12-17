def solution(prices):
    # init
    len_p = len(prices)
    times = [0 for _ in range(len_p)]
    st = []
    
    # 0 ~ N
    for i in range(len_p):
        if not st: # 비교할 값이 없다면
            st.append([prices[i],i+1])
            continue
        # ST이 있다면?
        while True:
            if st:
                if prices[i] < st[-1][0]:
                    st_p, st_i = st.pop()
                    times[st_i-1] = (i+1) - (st_i)
                    continue
                    
            st.append([prices[i], i+1])
            break
    while st: # st 비우기, 끝까지 다 돌았단 소리
        st_p, st_i = st.pop()
        times[st_i-1] = len_p - st_i
    
    return times