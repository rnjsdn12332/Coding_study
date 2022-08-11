#떡의 개수 N, 
#떡의 개별 높이가 들어있는 배열 cake_len 데이터의 총합은 M이상
import time
start_time=time.time()
n, m =map(int, input().split())
cake_len=list(map(int, input().split()))

cake_len=sorted(cake_len)

start=0
end=cake_len[-1]
result=0
while start<=end : 
    mid=(start+end)//2
    sum=0
    for i in cake_len :
        if i>mid :
            sum+=i-mid
    if sum < m : 
        end=mid-1
    elif sum > m : 
        start=mid+1
    else  :
        result=mid
        break
        
        

print(result)
