###### 문제 설명

게임개발자인 "죠르디"는 크레인 인형뽑기 기계를 모바일 게임으로 만들려고 합니다.
"죠르디"는 게임의 재미를 높이기 위해 화면 구성과 규칙을 다음과 같이 게임 로직에 반영하려고 합니다.

![crane_game_101.png](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/69f1cd36-09f4-4435-8363-b71a650f7448/crane_game_101.png)

게임 화면은 **"1 x 1"** 크기의 칸들로 이루어진 **"N x N"** 크기의 정사각 격자이며 위쪽에는 크레인이 있고 오른쪽에는 바구니가 있습니다. (위 그림은 "5 x 5" 크기의 예시입니다). 각 격자 칸에는 다양한 인형이 들어 있으며 인형이 없는 칸은 빈칸입니다. 모든 인형은 "1 x 1" 크기의 격자 한 칸을 차지하며 **격자의 가장 아래 칸부터 차곡차곡 쌓여 있습니다.** 게임 사용자는 크레인을 좌우로 움직여서 멈춘 위치에서 가장 위에 있는 인형을 집어 올릴 수 있습니다. 집어 올린 인형은 바구니에 쌓이게 되는 데, 이때 바구니의 가장 아래 칸부터 인형이 순서대로 쌓이게 됩니다. 다음 그림은 [1번, 5번, 3번] 위치에서 순서대로 인형을 집어 올려 바구니에 담은 모습입니다.

![crane_game_102.png](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/638e2162-b1e4-4bbb-b0d7-62d31e97d75c/crane_game_102.png)

만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 됩니다. 위 상태에서 이어서 [5번] 위치에서 인형을 집어 바구니에 쌓으면 같은 모양 인형 **두 개**가 없어집니다.

![crane_game_103.gif](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/8569d736-091e-4771-b2d3-7a6e95a20c22/crane_game_103.gif)

크레인 작동 시 인형이 집어지지 않는 경우는 없으나 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다. 또한 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정합니다. (그림에서는 화면표시 제약으로 5칸만으로 표현하였음)

게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때, 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.

##### **[제한사항]**

- board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다.
- board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
  - 0은 빈 칸을 나타냅니다.
  - 1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
- moves 배열의 크기는 1 이상 1,000 이하입니다.
- moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.

##### **입출력 예**

| board                                                        | moves             | result |
| ------------------------------------------------------------ | ----------------- | ------ |
| [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]] | [1,5,3,5,1,2,1,4] | 4      |

##### **입출력 예에 대한 설명**

**입출력 예 #1**

인형의 처음 상태는 문제에 주어진 예시와 같습니다. 크레인이 [1, 5, 3, 5, 1, 2, 1, 4] 번 위치에서 차례대로 인형을 집어서 바구니에 옮겨 담은 후, 상태는 아래 그림과 같으며 바구니에 담는 과정에서 터트려져 사라진 인형은 4개 입니다.

![crane_game_104.jpg](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/bb0f59c7-6b72-485a-8302-217fe53ea88f/crane_game_104.jpg)

## 접근법

- `moves` : 크레인 옮기는 위치 (가장 위에 있는거 집기)
- `board` : 인형이 있는 공간
- `ylen, xlen` : board의 크기를 나타내는 수
- `lane` : 각 레인이 가지고 있는 개수

`moves`대로 움직이면서 st에 쌓는 것, 만약에 top에 있는 인형과 동일한 인형이라면 pop 하고, 뽑은 것도 넣지 않는다. 그리고 사라진 인형의 개수를 체크 (터지면 2개씩 사라짐)

## 정답

```python
def solution(board, moves):
    answer = 0
    x_len = len(board[0])
    y_len = len(board)
    # 레인 별 개수 체크
    lane = [0] * x_len
    
    for i in range(x_len):
        count = 0
        for j in range(y_len):
            if board[j][i] != 0:
                count+=1
        lane[i] = count
    
    st = []
    for m in moves:
        if lane[m-1] == 0:
            continue
        pos_y, pos_x = x_len-lane[m-1], m-1
        select = board[pos_y][pos_x]
        board[pos_y][pos_x] = 0
        lane[m-1]-=1
        if st:
            if st[-1] == select:
                st.pop()
                answer+=2
                continue
        
        st.append(select)
        
    return answer
```

- 우선 lane별로 개수를 파악
- 그리고 움직이면서 board를 0으로 처리해주면서 st에 넣고 같은 2개가 동시에 들어오면 터지게 함
- 하지만 여기서 위 lane별 개수를 파악 하지 않고 단순히 계산해도 충분히 코드를 효율적으로 짤 수 있음

```python
for m in moves:
    for j in range(len(board)): # y열로 내려감
        if board[j][m-1] != 0:
            st.append(board[j][m-1])
            board[j][m-1] = 0

            if len(st) > 1: # (2개 이상 이라는 뜻)
                if st[-1] == st[-2]:
                    st.pop()
                    st.pop()
                    answer+=2
```

- 이렇게 풀면 더 효율적으로 짧게 짤 수 있다.

