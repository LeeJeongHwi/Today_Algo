from sys import stdin
stdin = open("input.txt","r")

N = int(stdin.readline())

count = 0
number = 666
while True:
    if "666" not in str(number):
        number+=1
        continue
    count+=1
    if count == N:
        break
    number+=1
print(number)