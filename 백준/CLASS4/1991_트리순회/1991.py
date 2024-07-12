from sys import stdin
stdin = open('input.txt')
n = int(stdin.readline())

# 전위 : root -> left -> right 순
# 중위 : left leaf -> root -> right leaf 순
# 후위 : left leaf -> right leaf -> root

nodes = {}

for _ in range(n):
    value, left, right = stdin.readline().split()
    nodes[value] = [left, right]

def pre_traversal(node):
    print(node, end="")
    if nodes[node][0] != ".": # Left Node Travel
        pre_traversal(nodes[node][0])
    if nodes[node][1] != ".": # right Node Travel
        pre_traversal(nodes[node][1])

def in_traversal(node):
    if nodes[node][0] != ".": # Left Node Travel
        in_traversal(nodes[node][0])
    print(node, end="")
    if nodes[node][1] != ".": # right Node Travel
        in_traversal(nodes[node][1])

def post_traversal(node, ):
    if nodes[node][0] != ".": # Left Node Travel
        post_traversal(nodes[node][0])
    if nodes[node][1] != ".": # right Node Travel
        post_traversal(nodes[node][1])
    print(node, end="")
    
pre_traversal("A")
print()
in_traversal("A")
print()
post_traversal("A")
