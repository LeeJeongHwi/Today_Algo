from sys import stdin

stdin = open("input.txt")

while True:
    num = stdin.readline().rstrip()
    if num == "0":
        break

    l_num = len(num)
    mid = len(num)//2
    flag = True
    for i in range(mid):
        if num[i] != num[l_num-i-1]:
            flag = False
            break
    
    print("yes") if flag else print("no")
    
# num[::-1] 로 뒤집은 값이랑 입력받은 값이랑 다르면 팰린드롬이 아니다..로 구현하면 더 빠름