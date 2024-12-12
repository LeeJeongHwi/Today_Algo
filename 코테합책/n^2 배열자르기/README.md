# n^2 배열 자르기

###### 문제 설명

정수 `n`, `left`, `right`가 주어집니다. 다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.

1. `n`행 `n`열 크기의 비어있는 2차원 배열을 만듭니다.

2. ```
   i = 1, 2, 3, ..., n
   ```

   에 대해서, 다음 과정을 반복합니다.

   - 1행 1열부터 `i`행 `i`열까지의 영역 내의 모든 빈 칸을 숫자 `i`로 채웁니다.

3. 1행, 2행, ..., `n`행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.

4. 새로운 1차원 배열을 `arr`이라 할 때, `arr[left]`, `arr[left+1]`, ..., `arr[right]`만 남기고 나머지는 지웁니다.

정수 `n`, `left`, `right`가 매개변수로 주어집니다. 주어진 과정대로 만들어진 1차원 배열을 return 하도록 solution 함수를 완성해주세요.

------

##### 제한사항

- 1 ≤ `n` ≤ 10^7
- 0 ≤ `left` ≤ `right` < n2
- `right` - `left` < 10^5

------

##### 입출력 예

| n    | left | right | result              |
| ---- | ---- | ----- | ------------------- |
| 3    | 2    | 5     | `[3,2,2,3]`         |
| 4    | 7    | 14    | `[4,3,3,3,4,4,4,4]` |



## 접근법

배열을 만드는게 제일 우선 해결해야될 일

0,0부터 시작해서 [0,1],[1,0],[1,1] -> [0,2],[2,0],[2,2],

최대 n은`10000000`

1 - 3 - 5 - 7 -9... 2개씩 증가함

[0,0] -> [0,1],[1,1],[1,0] -> [0,2],[1,2],[2,2],[2,1],[2,0]

deque로 일단 배열 만들기 한 뒤 시간초과 날 시 새로운 방법 찾아보기

```python
def solution(n, left, right):
    maps = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append([0,0])
    maps[0][0] = 1
    # 이동할 지점은 [(0,1),(1,0),(1,1)]
    while q:
        now_y, now_x = q.popleft()
        for dy, dx in [(0,1),(1,0),(1,1)]:
            ny = now_y + dy
            nx = now_x + dx
            if (ny < n) and (nx < n) and maps[ny][nx] == -1:
                maps[ny][nx] = maps[now_y][now_x]+1
                q.append([ny,nx])
    
    # extend?
    answers = []
    for map in maps:
        answers.extend(map)
    
    return answers[left:right+1]
```

- 하지만 이 방법은 시간초과가 난다.. 아무래도 extend나 q로 map을 설정하는 과정에서 난듯
- 그러면 extend 없이 어떻게 하는가부터 보자

```python
answers = []
count = 0
for i in range(n):
    for j in range(n):
        if (left<= count <=right):
            answers.append(maps[i][j])
        count+=1
return answers
```

- 하지만 이것도 시간초과

그러면 배열 채우는 것을 바꿔야함

어떻게하면 O(n)방식으로 배열을 채울 수 있을까?

일단 이 2차원 배열의 규칙은..

```python
1
22
333
4444
55555
....
에서
2345
345
45
5
-
```

이렇게 코드를 짤 수 있다

```python
for i in range(n):
    number = i+1
    for j in range(i+1): # 앞 채우기
        maps[i][j] = number

    for k in range(i+1, n): # 뒤 채우기
        maps[i][k] = k+1
```

- 줄어들긴했지만... 여전히 테케2~3, 9~ 부터는 계속 시간초과가 발생

어떻게 풀어야할지 감이 안와서 질문하기 참고

```python
`2차원 배열에서 좌표마다 어떤값이 들어가는지 적어보시면 좌표값만 보고도 어떤 숫자가 들어 있을지 알 수 있을거에요`

3x3 행렬일 때
(1,1) = 1 (1,2) = 2 (1,3) = 3
(2,1) = 2 (2,2) = 2 (2,3) = 3
(3,1) = 3 (3,2) = 3 (3,3) = 3

간단하게 각 좌표 x, y 값중 큰 값이 해당 값이 됩니다.
이제 주어지는 left ~ right 1차원 index 값을, 2차원 인덱스(x, y) 값으로 변환만 하시면 되겠네요?
```

- 배열을 다 채울 필요가 없다라는 것



### 정답 코드

```python
def solution(n, left, right):
    # 근데 채우지 않고 얻어내야함
    # n=4에서 2~5 라고 했을 때 i,j를 각각 구해야함

    # 2,3,4,5,6 이렇게 흘러가는데,
    # 0번째 인덱스는 행마다의 i가 나와야함
    # 1번쨰 인덱스는 열마다의 i가 나와야함
    # [1,3][1,4] [2,1][2,2][2,3]
    
    answers = []
    for i in range(left, right+1):
        answers.append(max([i//n+1,i%n+1]))
    
    return answers
```

- 규칙을 찾을 수가 있었다...

확실히 Lv2 부터 어렵다...



