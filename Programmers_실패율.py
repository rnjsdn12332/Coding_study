from collections import deque
def solution(N, stages):
    stages.sort()
    answer=[]
    people=len(stages)
    array=[]
    for i in range(1,N+1) :
        cnt=stages.count(i)
        if not people==0:
            array.append((i, cnt/people))
        else :
            array.append((i, 0))
        print(people, cnt)
        people-=cnt
    
    answer=sorted(array, key=lambda x:x[1], reverse=True)
    answer=[i[0] for i in answer]
    return answer
