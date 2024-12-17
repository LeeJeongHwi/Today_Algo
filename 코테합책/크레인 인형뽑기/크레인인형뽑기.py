def solution(board, moves):
    answer = 0
    x_len = len(board[0])
    y_len = len(board)
    # 레인 별 개수 체크
    lane = [0] * x_len
    
    for i in range(x_len):
        count = 0
        for j in range(y_len):
            if board[j][i] != 0:
                count+=1
        lane[i] = count
    
    st = []
    for m in moves:
        if lane[m-1] == 0:
            continue
        pos_y, pos_x = x_len-lane[m-1], m-1
        select = board[pos_y][pos_x]
        board[pos_y][pos_x] = 0
        lane[m-1]-=1
        if st:
            if st[-1] == select:
                st.pop()
                answer+=2
                continue
        
        st.append(select)
        
    return answer


