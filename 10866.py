import sys
from collections import deque
input=sys.stdin.readline
que=deque()

T=input()
for i in range(int(T)) :
    s=list(input().split())


    if s[0]=='push_back' :
        que.appendleft(s[1])
    elif s[0]=='push_front' :
        que.append(s[1])
    elif s[0]=='pop_front' :
        if len(que) > 0 :

            print(que.pop())
        else :
            print(-1)
    elif s[0]=='pop_back' :
        if len(que) > 0 :

            print(que.popleft())
        else :
            print(-1)
    elif s[0]=='size' :
        print(len(que))
    elif s[0]=='empty' :
        if len(que)>0 :
            print(0)
        else :
            print(1)
    elif s[0]=='front' :
        if len(que) > 0 :
            print(que[-1])
        else :
            print(-1)
    elif s[0]=='back' :
        if len(que) > 0 :
            print(que[0])
        else :
            print(-1)