from collections import deque
def solution(priorities, location):
    answer = 0
    i=0
    q=deque()
    for i,x in enumerate(priorities) :
        q.append((i,x))

    cnt=0
    while q:
        temp=q.popleft()
        if any(temp[1]<x[1] for x in q)  :
            q.append(temp)
        else :
            cnt+=1
            if temp[0]==location :
                answer=cnt

        
            
    return answer
