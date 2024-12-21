from sys import stdin
stdin = open('input.txt')

board = stdin.readline().split(".")

def solution(board):
    
    for b in board:
        