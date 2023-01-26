from sys import stdin

stdin = open("input.txt","r")

# () = 2 / [] = 3 / (x) = 2*x / [x] = 3*x / xy = x+y

def solution(bracket):
    if len(bracket)%2 != 0:
        return 0
    st = []
    for s in bracket:
        # print(st)
        if s not in ["(","[","]",")"]:
            return 0
        
        # (, [를 만나면 넣어버려
        if s in ['(','[']:
            st.append(s)
            continue
        # ) 만나면?
        if s == ")":
            if not st: # )가 들어왔는데 Stack에 암것도 없으면 올바르지 않은 괄호열
                return 0
            if st[-1] == "(":
                st.pop()
                st.append(2)
                continue
            nst = []
            while st:
                sp = st.pop()
                if sp == "(":
                    st.append(sum(nst)*2)
                    break
                if sp == "[":
                    return 0
                nst.append(sp)
        # ] 만나면?
        elif s == "]":
            if not st: # ]가 들어왔는데 Stack에 암것도 없으면 올바르지 않은 괄호열
                return 0
            if st[-1] == "[":
                st.pop()
                st.append(3)
                continue
            nst = []
            while st:
                sp = st.pop()
                if sp == "[":
                    st.append(sum(nst)*3)
                    break
                if sp == "(":
                    return 0
                nst.append(sp)

    # bracket을 다 돌렸는데 st에 괄호들이 남아있다면 False
    for rem in st:
        if rem in ["(",")","[","]"]:
            return 0


    return sum(st)
                    
line = stdin.readline().rstrip()
print(solution(line))



