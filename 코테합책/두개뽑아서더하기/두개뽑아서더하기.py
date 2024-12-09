def solution(numbers):
    # 중복값 제거를 위해 set으로 설정
    arr = set()
    # i,j를 돌면서 bubble sort처럼 선택
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            arr.add(numbers[i]+numbers[j])
    # 최종적으로 정답을 sort
    return sorted(list(arr))