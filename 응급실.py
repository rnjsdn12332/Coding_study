#첫줄에 자연수 n과 m이 주어짐
#두 번쨰 줄에 접수한 순서대로 환자의 위험도가 주어짐(50<-위험도<=100)
#접수한 순서대로 목록에서 제일 앞에 있는 환자목록을 꺼냄
#나머지 대기 목록에서 꺼낸 환자보다 위험도가 높은 환자가 존재하면 대기목록 제일 뒤로 다시넣음
#m번째 환자는 몇번째의 진료를 받게될까?

from collections import deque
n, m=map(int, input().split())
array=list(map(int, input().split()))

q=deque()
for index, val in enumerate(array) :
    q.append((index,val))

array_num=[]
cnt=0
while q :
    start=q.popleft()
    if any(start[1]<x[1] for x in q) :
        q.append(start)
    else :
        cnt+=1
        q.popleft()
        if start[0]==m :
            print(cnt)
            break


        