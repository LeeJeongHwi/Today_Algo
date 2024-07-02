n = int(input())
from math import sqrt

# 출입하는 사람과 충돌하지 않도록 오른쪽 벽 방향으로 적외선 신호를 발사 즉, q
# 최종 정답 : p+q
#거리
#시간, 속력
def solve():
	L,a,v = map(float,input().split())
	# s = 0.5* a * (t**2)
	time = sqrt(2*L/a)
	ans = round(v*time,2)
	print("{:.2f}".format(ans))
	
	
for _ in range(n):
	solve()
