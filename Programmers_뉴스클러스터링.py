def solution(str1, str2):
    A=[]
    B=[]
    for i in range(1,len(str1)) :
        if str1[i].isalpha() and str1[i-1].isalpha() :
            A.append((str1[i-1]+str1[i]).upper())
    for i in range(1,len(str2)) :
        if str2[i].isalpha() and str2[i-1].isalpha():
            B.append((str2[i-1]+str2[i]).upper())

    AA=set(A)
    BB=set(B)
    #교집합
    n=len(AA&BB)
    for k in AA&BB :
        n+=min(A.count(k), B.count(k))-1
    #합집합
    s=len(A)+len(B)-n
    if n==0 and s==0 :
        return 1*65536

    answer=n/s
    return int(answer*65536)
