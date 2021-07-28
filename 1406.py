'''
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
'''

#위 코드는 시간초과 문제 발생 시간복잡도 생각해서 insert를 빼고 pop, append로 짰더니 해결

import sys
input=sys.stdin.readline

s=list(input().strip())
n=int(input().strip())
stack2=[]

idx=len(s)
for i in range(n) :
    order=list(input().strip().split())


    if order[0] == 'L' and s != []:
        stack2.append(s.pop())
    elif order[0] == 'D' and stack2 != []:
        s.append(stack2.pop())
    elif order[0] == 'B' and s != []:
        s.pop()
    elif order[0] == 'P' :
        s.append(order[1])

print("".join(s+list(reversed(stack2))))
