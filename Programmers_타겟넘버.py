from collections import deque
def solution(numbers, target):
    answer=0
    stack=[[numbers[0],0], [numbers[0]*(-1),0]]
    while stack :
        temp, idx=stack.pop()
        idx+=1
        if idx<len(numbers) :
            stack.append([temp+numbers[idx],idx])
            stack.append([temp-numbers[idx],idx])
        else :
            if target==temp :
                answer+=1

    return answer