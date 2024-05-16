from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())

arr = [int(stdin.readline()) for _ in range(n)]
# Merge Sort (space : O(N), time : O(nlogn))

def merge_sort(arr):
    
    def sort(low, high): # divide
        if high - low < 2:
            return
        
        mid = (low + high)//2
        sort(low, mid) # 쪼개기 (하단)
        sort(mid, high) # 쪼개기 (상단)
        merge(low, mid, high) # 합병

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high: # l 이 mid보다 커지거나, h가 high보다 커질때 종료
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1
        while l < mid: # 남아 있는 것들 append
            temp.append(arr[l])
            l += 1
        while h < high: # 남아 있는 것들 append
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low] # i 자리에 정렬된 temp 배열을 넣는 작업
    return sort(0, n)

merge_sort(arr)
for a in arr:
    print(a)