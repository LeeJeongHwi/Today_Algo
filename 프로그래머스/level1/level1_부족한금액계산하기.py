def solution(price, money, count):
    p = 0
    for c in range(1, count+1):
        p += (price*c)
        
    if money - p < 0:
        return p - money
    else:
        return 0 