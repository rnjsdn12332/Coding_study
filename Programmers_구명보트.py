from collections  import deque
def solution(people, limit):
    people.sort(reverse=True)
    q=deque(people)
    cnt=0
    while q :
        sub=limit-q.popleft()
        while q and q[-1]<=sub :
            sub-=q.pop()
        cnt+=1
        
                
                
    
    return cnt
