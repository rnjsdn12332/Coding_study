def solution(n):
    answer = 1
    if n%2==0 :
        answer+=2**(n/2)
    else :
        answer+=2**((n-1)/2)
        
    return answer%1000000007
