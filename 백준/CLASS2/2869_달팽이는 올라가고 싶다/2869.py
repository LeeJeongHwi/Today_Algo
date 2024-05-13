from sys import stdin
import math
stdin = open('input.txt')

A,B,V = map(int,stdin.readline().split())

# V/(A-B)-1 < Day

print(math.ceil((V-B)/(A-B)))