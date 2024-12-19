def init(n): # LinkedList init
    nodes = []
    # prev, now, next
    for i in range(n):
        if i==0:
            node = [None, 0, i+1, "O"]
        elif i == n-1:
            node = [i-1, i, None, "O"]
        else:
            node = [i-1, i, i+1, "O"]
        nodes.append(node)
    return nodes

"""
"U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
"D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
"C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
"Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
"""

def solution(n,k,cmd):
    #LikedList init
    nodes = init(n)
    del_st = []
    for command in cmd:
        c = command.split()
        if c[0] == "U": # prev로 이동
            for i in range(int(c[1])):
                k = nodes[k][0]

        elif c[0] == "D": # next로 이동
            for i in range(int(c[1])):
                k = nodes[k][2]

        elif c[0] == "C": # 지울 때 현재 행보다 위에 있는 애의 next를 현재 행의 next로 이어주고, 다음 행의 prev를 현재행의 prev로 이어줌

            if nodes[k][0] is not None:
                nodes[nodes[k][0]][2] = nodes[k][2] # prev node change
            if nodes[k][2] is not None:
                nodes[nodes[k][2]][0] = nodes[k][0] # next node change

            nodes[k][3] = "X"
            del_st.append(nodes[k])
            if nodes[k][2] is not None: # 현재 행이 마지막행이 아닐 때, 바로 아래 행(next)을 k로 선정
                k = nodes[k][2]
            else: # 현재 행이 마지막행이면 바로 위의 행을 선택
                k = nodes[k][0]

        elif c[0] == "Z": # 복구할 땐 st에서 node를 가져옴
            resto_node = del_st.pop()
            nodes[resto_node[1]][3] = "O" # 복구
            # resto_node와 연결된 prev node의 next를 resto_node로 바꾸기
            if resto_node[0] is not None:
                nodes[resto_node[0]][2] = resto_node[1]
            # resto_node와 연결된 next node의 prev를 resto_node로 바꾸기
            if resto_node[2] is not None:
                nodes[resto_node[2]][0] = resto_node[1]

    answer = []
    for node in nodes:
        answer.append(node[3])

    return "".join(answer)



# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
# print(solution(5, 1, ["C","C","C","C","C"]))
print(solution(5, 4, ["C","C","C","U 1","C","Z"]))
