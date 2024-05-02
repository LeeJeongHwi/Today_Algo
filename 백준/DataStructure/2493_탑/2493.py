from sys import stdin
stdin = open("input.txt","r")
def solution(n, line):
    st = []
    result = [0 for _ in range(n)]
    for i, tower in enumerate(line): 
        if i == 0 :
            st.append([tower,i])
            continue        

        if st[-1][0] > tower:
            result[i] = st[-1][1]+1
            st.append([tower,i])
            continue
    
        now = tower # 현재 선택된 타워
        
        while True:
            # print(st)
            if st:
                prev = st[-1][0] # Stack안에 있는 타워 (비교해야할 대상)
            else:
                st.append([tower, i])
                break

            if prev > tower:
                result[i] = st[-1][1]+1
                st.append([tower,i])
                break
            elif prev < tower:
                st.pop()
                if st:
                    prev = st[-1][0]
                    continue

    print(" ".join(map(str,result)))

n = int(stdin.readline().rstrip())
line = list(map(int,stdin.readline().split()))
solution(n, line)