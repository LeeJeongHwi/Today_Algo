n = int(input())
scores = [[x,i+1] for i,x in enumerate(map(int,input().split()))]

scores.sort(key=lambda x:-x[0])
print(scores[0][1],scores[1][1],scores[2][1],)
