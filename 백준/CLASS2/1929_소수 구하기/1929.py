from math import sqrt
from sys import stdin
stdin = open('input.txt')

m, n = map(int,stdin.readline().split())


def prior(num1,num2):

    priors = [0 for _ in range(num2+1)]
    priors[1] = 1
    priors[0] = 1
    for i in range(2, int(sqrt(num2))+1):
        if priors[i] != 1:
            for j in range(i+i, num2+1, i):
                priors[j] = 1
    
    for i in range(num1,num2+1):
        if priors[i] == 0:
            print(i)

prior(m,n)
