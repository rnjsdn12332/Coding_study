def solution(n):
    answer = 0
    max_val=n//2
    one=1
    two=2
    if n==1:
        return one
    elif n==2:
        return two
    for i in range(n-2):
        temp=one
        one=two
        two=one+temp
    answer=two%1000000007
    return answer
