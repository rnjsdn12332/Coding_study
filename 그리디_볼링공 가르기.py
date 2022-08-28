'''from collections import deque

n, m=map(int, input().split())
s=list(map(int, input().split()))


q=deque(s)
cnt=0
while q :
    temp=q.popleft()
    for i in q :
        if i!=temp :
            cnt+=1

print(cnt)'''

n, m=map(int, input().split())
s=list(map(int, input().split()))

#1부터 10까지 무게를 담을 수 있는 리스트
array=[0]*11

#볼링공 무게 기록
for x in s :
    array[x]+=1 

result =0

for i in range(1, m+1) :
    n-=array[i] #무게가 i인 볼링공의 개수 제외
    result+=array[i]*n #b가 선택한 경우의 수와 곱하기

print(result)
