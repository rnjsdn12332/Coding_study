from collections import deque

def solution(progresses, speeds):
    answer = []
    array=[]
    speed=0
    for i in range(len(progresses)) :
        #남은 양
        temp=100-progresses[i]
        #걸리는 시간
        if temp%speeds[i] :
            speed=temp//speeds[i]+1
        else :
            speed=temp//speeds[i]
        array.append(speed)
    
    q=deque(array)
    
    while q :
        cnt=1
        start=q.popleft()
        for x in q :
            if x<=start :
                cnt+=1
            else :
                break
        if cnt>1 :
            for i in range(cnt-1) :
                q.popleft()
        answer.append(cnt)

    return answer