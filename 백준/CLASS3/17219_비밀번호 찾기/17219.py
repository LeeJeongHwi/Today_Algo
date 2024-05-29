from sys import stdin
stdin = open('input.txt')

n, m = map(int,stdin.readline().split())

sites = {}

for _ in range(n):
    site, pwd = stdin.readline().split()
    sites[site] = pwd

for _ in range(m):
    site = stdin.readline().rstrip()
    print(sites[site])