import sys
input=sys.stdin.readline

s=list(input().strip())
n=int(input())


idx=len(s)
for i in range(n) :
    order=list(input().strip().split())


    if order[0] == 'L' :
        idx-=1
    elif order[0] == 'D' :
        if idx <=len(s)+1 :
            idx+=1
    elif order[0] == 'B' :
        if idx > 0 and idx<len(s):
            s.pop(idx-1)
            idx-=1
    else :
        s.insert(idx, order[1])
        idx+=1

print(('').join(s))
