from math import gcd
def solution(arr):
    answer=arr[0]
    
    for a in arr :
        answer=answer*a//gcd(answer, a)
    
    
    return answer
