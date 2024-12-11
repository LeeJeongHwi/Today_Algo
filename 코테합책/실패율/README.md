## 실패율

슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다. 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.

이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다. 역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다. 오렐리를 위해 실패율을 구하는 코드를 완성하라.

- 실패율은 다음과 같이 정의한다.
  - 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

##### 제한사항

- 스테이지의 개수 N은 `1` 이상 `500` 이하의 자연수이다.
- stages의 길이는 `1` 이상 `200,000` 이하이다.
- stages에는`1`이상`N+1`이하의 자연수가 담겨있다.
  - 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
  - 단, `N + 1` 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
- 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
- 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 `0` 으로 정의한다.

##### 입출력 예

| N    | stages                   | result      |
| ---- | ------------------------ | ----------- |
| 5    | [2, 1, 2, 6, 2, 4, 3, 3] | [3,4,2,1,5] |
| 4    | [4,4,4,4,4]              | [4,1,2,3]   |

##### 입출력 예 설명

입출력 예 #1
1번 스테이지에는 총 8명의 사용자가 도전했으며, 이 중 1명의 사용자가 아직 클리어하지 못했다. 따라서 1번 스테이지의 실패율은 다음과 같다.

- 1 번 스테이지 실패율 : 1/8

2번 스테이지에는 총 7명의 사용자가 도전했으며, 이 중 3명의 사용자가 아직 클리어하지 못했다. 따라서 2번 스테이지의 실패율은 다음과 같다.

- 2 번 스테이지 실패율 : 3/7

마찬가지로 나머지 스테이지의 실패율은 다음과 같다.

- 3 번 스테이지 실패율 : 2/4
- 4번 스테이지 실패율 : 1/2
- 5번 스테이지 실패율 : 0/1

각 스테이지의 번호를 실패율의 내림차순으로 정렬하면 다음과 같다.

- [3,4,2,1,5]

입출력 예 #2

모든 사용자가 마지막 스테이지에 있으므로 4번 스테이지의 실패율은 1이며 나머지 스테이지의 실패율은 0이다.

- [4,1,2,3]



# 접근법

실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

전체 스테이지 `N`과 사용자가 멈춰있는 `stage`가 매개변수로 주어진다.

실패율이 높은 스테이지부터 내림차순

스테이지 개수는 최대 500, 참여한 사람들의 수는 200,000로

최대 $$O(500*200,000) = O(100,000,000)$$ 으로 $$O(N^2)$$을 보이는 것으로 확인된다.

알고리즘은 다음과 같다.

- Stage마다 인원체크를 하기위해 1 ~ N (i) 까지 Iteration을 돈다

- 우선은 그 스테이지에 도달한 사람부터 체크를 한다 -> i스테이지보다 작은 수는 제외한 인원수 체크
  - 그리고 새로운 배열에 계속 추가해서 스테이지마다 보는 수를 줄이는 것은 어떨까? `clear_person`을 지속적으로 갱신
- 그리고 스테이지와 수가 같으면 `클리어 못한 수 (fail_person)` 을 증가

- 계산한 실패율은 `failure`에 저장
- 마지막에 내림차순으로 Sort

## 통과 코드

```python
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
```

### 나의 예전풀이..

```python
def solution(n,stages):
    ans = []
    for i in range(1,n+1):
        chal = 0
        err = 0
        for s in stages:
            if s>=i:
                chal+=1
            if s==i:
                err+=1
        if chal == 0:
            ans.append((0,i))
        else:
            ans.append(((err/chal),i))
    ans.sort(reverse=True,key=lambda x:(x[0],-x[1]))
    return [x[1] for x in ans]
```



## 다른 Solution 코드 분석

```python
def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):])
        yet = info[i + 1]
        if be == 0:
            fail.append((str(i + 1), 0))
        else:
            fail.append((str(i + 1), yet / be))
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
    return answer
```

- 왜 굳이 stage수+2만큼 한걸까?
- info는 시도했지만 아직 클리어하지 못한 사람의 수를 나타낸다
- be는 시도한 전체 인원
- yet은 해당 스테이지에서 클리어하지 못한 사람들의 수
- be가 0이면 아무도 시도하지 않은거니까 0 추가
  - 아니라면 실패율 계산

