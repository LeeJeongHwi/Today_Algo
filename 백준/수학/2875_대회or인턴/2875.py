from sys import stdin
#stdin = open('input.txt')

N, M, K = map(int,stdin.readline().split())

# K 명은 꼭 참여
# 여학생은 2, 남학생은 1

# 먼저 대회갈사람 먼저 빼놓는데, 총합이 K보다 작아야함
def solution(N, M, K):
    count = 0
    while True:
        N-=2
        M-=1
        
        if N + M < K: # 인턴십으로 빼야될 수
            break

        if N >= 0 and M >= 0: # 더이상 못만드는 경우
            count += 1
        else:
            break
    
    print(count)

solution(N,M,K)