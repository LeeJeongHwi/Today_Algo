from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())
users = []
for i in range(n):
    line = stdin.readline().split()
    users.append([int(line[0]),line[1]])

users.sort(key=lambda x: (x[0]))

for user in users:
    print(user[0],user[1])