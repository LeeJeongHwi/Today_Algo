from sys import stdin

stdin = open("input.txt")

n = int(stdin.readline().rstrip())
numbers = list(map(int,stdin.readline().split()))
count = 0

# 굳이 Num까지 볼 필요가 없다. 
# 소수는 1~ N제곱근 까지 있기 때문 (나머진 대칭)

def find_prior(num):
    flag = True
    for i in range(2, num):
        if num%i == 0: # 나누어 떨어진다는 뜻
            flag = False
            return flag
    return flag

for number in numbers:
    if number == 1:
        continue
    if find_prior(number):
        count+=1

print(count)


