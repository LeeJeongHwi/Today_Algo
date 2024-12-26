from sys import stdin
stdin = open('input.txt')

N = int(stdin.readline())

# 거리 1km당 1리터 기름
# 도시에 있는 주유소 리터당 가격, 간선은 거리

dist = list(map(int,stdin.readline().split()))
city = list(map(int,stdin.readline().split()))

def solution(N, dist, city):
    # i = 0
    price = 0
    now_city = city[0]

    # while i<N-1:
    #     now_city = city[i]
    #     total_dist = dist[i]
    #     while i<N-2:
    #         if now_city < city[i+1]:
    #             total_dist += dist[i+1]
    #             i+=1
    #         else:
    #             break
    #     price += total_dist * now_city

    for i in range(0, N-1):
        # print("Now city", now_city)
        # print("dist", dist[i])
        price += (now_city * dist[i])
        if now_city > city[i+1]: # 도시 변경
            # print("Change city", now_city, city[i+1])
            now_city = city[i+1]
    return price
            


print(solution(N, dist, city))