from sys import stdin
stdin = open('input.txt')

# 1,000,000개의 데이터, 256MB제한
# O(nlogn) 속도를 보장하는 Merge sort 사용
# Quick Sort로도 되나?

n = int(stdin.readline())
numlist = [int(stdin.readline()) for _ in range(n)]

def merge_sort(numlist):
    def sort(l,h):
        if h-l < 2:
            return
        
        mid = (l+h)//2
        sort(l,mid)
        sort(mid,h)
        merge(l,mid,h)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if numlist[l] < numlist[h]:
                temp.append(numlist[l])
                l+=1
            else:
                temp.append(numlist[h])
                h+=1

        while l < mid :
            temp.append(numlist[l])
            l+=1

        while h < high :
            temp.append(numlist[h])
            h+=1
        
        for i in range(low, high):
            numlist[i] = temp[i - low]
    
    return sort(0, n)

merge_sort(numlist)
for a in numlist:
    print(a)

# 근데 계수정렬로도 충분히 빠른속도가 나옴;;; 굳이 Merge 소트 안해도됨