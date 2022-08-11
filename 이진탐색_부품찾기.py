#N개의 숫자가 들어있는 배열 A
#M개의 숫자가 들어있는 배열 B
# A에 B에 있는 데이터와 일치한 것이 있는지 확인

#이진탐색으로 풀어야겠다

#이진탐색 함수
def bineory_search(array, target, start, end) :
    mid=(start+end)//2
    if start>end :
        return None
    else :
        if array[mid]==target :
            return mid
        elif array[mid]<target :
            return bineory_search(array, target, mid+1, end)
        elif array[mid]>target : 
            return bineory_search(array, target, start, mid-1)
    return None

n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))
a=sorted(a)

#m의 데이터를 하나씩 이진탐색 함수에 넣고 결과출력
for i in range(m) :
    result=bineory_search(a, b[i], 0, n-1)
    if result==None :
        print("no", end=" ")
    else :
        print("yes", end=" ")
