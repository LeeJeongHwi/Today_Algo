def solution(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    answer = []
    
    for i in range(r1):
        row = []
        for k in range(c2):
            value = 0
            for j in range(c1):
                arr1_value = arr1[i][j]
                arr2_value = arr2[j][k]
                value += arr1_value * arr2_value
            row.append(value)
        
        answer.append(row)
    
    return answer