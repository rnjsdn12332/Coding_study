from collections import deque
def solution(arr):
    answer = []
    q=deque(arr)
    temp=q.popleft()
    answer.append(temp)
    while q:
        if temp == q[0] :
            temp=q.popleft()
        else :
            temp=q.popleft()
            answer.append(temp)
    return answer
