from sys import stdin
stdin = open('input.txt')

comp = int(stdin.readline())
n_node = int(stdin.readline())

comp_nodes = [0 for _ in range(comp+1)]
nodes = {}

for _ in range(n_node):
    a, b = map(int, stdin.readline().split())

    if a not in nodes:
        nodes[a] = [b]
    else:
        nodes[a].append(b)

    if b not in nodes:
        nodes[b] = [a]
    else:
        nodes[b].append(a)


def dfs(n):
    st = [n]
    count = 0
    comp_nodes[n] = 1
    while st:
        now = st.pop()
        for node in nodes[now]:
            if comp_nodes[node] != 1:
                st.append(node)
                count+=1
                comp_nodes[node] = 1
    
    return count

if n_node != 0:
    print(dfs(1))
else:
    print(0)
            