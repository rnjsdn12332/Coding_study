from collections import deque
def solution(numbers):  
    num=list()
    for i in numbers : 
        num.append(str(i))
    num=sorted(num, reverse=True, key=lambda x : x*3)
            
    answer=str(int("".join(num)))
    return answer
