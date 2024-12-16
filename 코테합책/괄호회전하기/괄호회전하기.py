from collections import deque
def check_bracket(rotated_s):
    st = []
    bracket = {"]":"[","}":"{",")":"("}
    for b in rotated_s:
        # inner bracket이면 st에 추가
        if b in bracket.values():
            st.append(b)
            continue
        # out bracket이면 st top의 inner brakcet모양과 같은지 확인
        if st: # st에 아무것도 없는데 out bracket이 나오기 때문에 False
            top = st.pop()
        else: 
            return False
        
        if top != bracket[b]:
            return False    
        continue
        
    if not st: # st에 비어있는지 확인
        return True
    else:
        return False
    
def solution(s):
    answer = 0
    s_len = len(s)
    q = deque([x for x in s])
    for i in range(s_len):
        #Rotate
        if i == 0:
            pass
        elif i != 0:
            tmp = q.popleft()
            q.append(tmp)
            
        if check_bracket(q):
            answer+=1
            
    return answer