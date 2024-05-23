from sys import stdin
stdin = open('input.txt')

k = int(stdin.readline())

st = []
for _ in range(k):
    n = int(stdin.readline())

    if n != 0 :
        st.append(n)
    elif n == 0:
        st.pop()
    
print(sum(st))