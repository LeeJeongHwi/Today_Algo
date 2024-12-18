# 주식 가격

###### 문제 설명

초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

##### 제한사항

- prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
- prices의 길이는 2 이상 100,000 이하입니다.

##### 입출력 예

| prices          | return          |
| --------------- | --------------- |
| [1, 2, 3, 2, 3] | [4, 3, 1, 1, 0] |

##### 입출력 예 설명

- 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
- 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
- 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
- 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
- 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.

※ 공지 - 2019년 2월 28일 지문이 리뉴얼되었습니다.



## 접근법

일단 지문을 이해하자

"초 단위로 기록된 주식 가격이 담긴 배열 prices", 즉 prices의 0번째 값에서 값이 떨어지는 index까지의 길이를 반환하면 된다.

1초는 현재 1원 -> 그 뒤 배열을 봤을 때 1보다 작은 수가 있는지 확인했을 때 없다 -> 끝까지 안떨어지니까 1초 이후 4초간 지속 됐다해서 4가나옴

$$O(N^2)$$로 풀 수 있는 방법은 0번째 -> 그 이후 탐색, 자기보다 작은 수 있으면 그 지점과 현재 위치와의 거리 계산

하지만, 최대 100000인 경우에, 100,000 * 100,000이 되므로, 시간 초과가 발생한다

즉 $$O(N)$$으로 해결할 수 있는 방법으로 찾아야함

- 스택으로 접근

time array : 0으로 구성된 N개의 배열

stack에는 (price, index+1)을 저장

top 보다 작은 price가 들어오면 현재의 index+1에서 저장된 시점의 index+1을 빼서 index+1-1의 위치에 저장



### 코드

```python
def solution(prices):
    # init
    len_p = len(prices)
    times = [0 for _ in range(len_p)]
    st = []
    
    # 0 ~ N
    for i in range(len_p):
        if not st: # 비교할 값이 없다면
            st.append([prices[i],i+1])
            continue
        # ST이 있다면?
        while True:
            if st:
                if prices[i] < st[-1][0]:
                    st_p, st_i = st.pop()
                    times[st_i-1] = (i+1) - (st_i)
                    continue
                    
            st.append([prices[i], i+1])
            break
    while st: # st 비우기, 끝까지 다 돌았단 소리
        st_p, st_i = st.pop()
        times[st_i-1] = len_p - st_i
    
    return times
```

