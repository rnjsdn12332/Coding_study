import sys
input=sys.stdin.readline

T=int(input())
for i in range(T) :
    s=list(input().strip())
    a=[]

    if s[0] == ')' :
        print("NO")
    else :
        for j in range(len(s)) :
            if s[j]=='(' :
                a.append(s[j])
            elif s[j]==')' :
                if len(a)>0 :
                    if a[-1]=='(' :
                        a.pop(-1)
                else :
                    a.append(s[j])
        if len(a)>0 :
            print("NO")
        else :
            print("YES")





