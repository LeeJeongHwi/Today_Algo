def solution(N, stages):
    failure = []
    
    clear_person = [x for x in stages] # 이 스테이지를 통과한 사람있는 배열
    remain_count = len(stages)
    # 1~N 까지 iter
    for stage in range(1,N+1):
        remain_person = []
        # 성공한 사람과 현재 남아있는 사람 비교
        fail_person = 0
        for person in clear_person:
            if stage == person: # 이 스테이지가 최대인 사람 -> remain_person에 못들어감
                fail_person += 1
            elif stage < person: # 이 스테이지를 통과한 사람
                remain_person.append(person)
        
        failure.append([stage,float(fail_person/remain_count)]) # 스테이지마다 실패율 기록
        remain_count -= fail_person
        if remain_count == 0: # 남아있는 유저가 없고 앞으로도 없을거임
            for i in range(N-stage): #남아있는 스테이지 싹다 0
                failure.append([stage+i+1,0])
            break
        clear_person = remain_person # 이렇게해야 시간초과 안뜸
    failure.sort(key=lambda x:-x[1])
    print(failure)
    return [x for x,fail in failure]

solution(5,[1,2,3,2,1])
    