def solution(n):
    answer = 0
    strn=str(n)
    length=len(strn)
    
    for i in range(length) :
        answer+=int(strn[i])
    return answer
