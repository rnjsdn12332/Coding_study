from collections import deque
def solution(s):
    qs=deque()
    qe=deque()
    for char in s : 
        if char=="(" :
            qs.append(1)
        else : 
            qe.append(1)
            if len(qs)<len(qe) :
                return False
            qs.popleft()
            qe.popleft()
            
    if qe or qs : 
        return False
    return True