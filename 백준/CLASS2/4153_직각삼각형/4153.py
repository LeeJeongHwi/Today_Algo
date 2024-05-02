while True:
    # a, b, c 중 뭐가 큰지 모르기 때문에, 정렬해서 a,b,c로 입력
    a, b, c = sorted(list(map(int,input().split())))
    if a==0 and b==0 and c==0:
        break
    if (a**2 + b**2) == c**2:
        print("right")
    else:
        print("wrong")