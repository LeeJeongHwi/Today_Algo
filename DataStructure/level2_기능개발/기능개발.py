from collections import deque


def solution(progresses, speeds):
    
    q = deque()
    ans = []
    max_days = 0
    count = 0
    for i, progress in enumerate(progresses):
        rem_pro = 100-progress
        if rem_pro%speeds[i]!=0:
            days = (rem_pro//speeds[i])+1
        else:
            days = (rem_pro//speeds[i])

        # Q에 없는 경우
        if not q:
            q.append([rem_pro, days])
            max_days = days
            count+=1
            continue
    
        # Q에 있는 경우
        if q[-1][1] > days:
            q.append([rem_pro, days])
            count += 1

        elif q[-1][1] <= days:        
            if max_days >= days:
                q.append([rem_pro, days])
                count +=1
            else:
                ans.append(count)
                max_days = days
                q = deque()
                q.append([rem_pro, days])
                count = 1
    if q:
        ans.append(count)

    
    return ans
    
print(solution([93, 30, 55], [1,30,5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([80, 70, 50, 40, 30, 20, 10], [1, 1, 1, 1, 1, 1, 1]))
print(solution([98, 99, 98, 98, 97], [1, 1, 1, 1, 1])) # 4, 1
