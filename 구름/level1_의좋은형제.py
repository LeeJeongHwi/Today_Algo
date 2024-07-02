jin, sun = map(int,input().split())
n = int(input())

for i in range(1,n+1):
	if i%2 != 0: # 진우 차례
		if jin%2 == 0:
			jin = jin//2
			sun += jin
		else:
			jin = jin//2
			sun += jin + 1
	else: # 선우 차례
		if sun%2 == 0:
			sun = sun//2
			jin += sun
		else:
			sun = sun//2
			jin += sun + 1
print(jin,sun)

# 솔직히 "가지고 있는 식량의 양이 홀수라서 반으로 나눌 수 없는 경우 그 식량을 통쨰로 넘겨준다" 이딴 말 삭제해야함 ㅡㅡ