from sys import stdin

stdin = open("input.txt","r")

# idx : 현재의 Target
# count : 현재 들어가는 숫자


n = int(stdin.readline())
st = []
target = [int(stdin.readline()) for _ in range (n)]
prints = []
count = 1 # 현재 Stack에 넣는 숫자
idx = 0 # 현재 타겟
flag = True

# 4 3 6 8 7 5 2 1

while 1:
   if count > n: # Count 숫자가 커지게 되면 append할거 다 했다는 뜻
      if st and idx < n:
         if st[-1] == target[idx]:
            st.pop()
            idx+=1
            prints.append("-")
            continue
         else:
            break
      break

   tg = target[idx]
   if tg == count: # 타겟과 들어오는 숫자가 똑같은 경우
      prints.append("+")
      prints.append("-")
      idx+=1
      count+=1
      continue

   else:
      if st:
         if st[-1] == tg: # pop해야됨
            st.pop()
            idx+=1
            prints.append("-")
         elif st[-1] != tg:
            st.append(count)
            count+=1
            prints.append("+")
      else: # 스택에 아무것도 없는 경우
         st.append(count)
         count+=1
         prints.append("+")
         
if st:
   print("NO")
else:
   print("\n".join(prints))