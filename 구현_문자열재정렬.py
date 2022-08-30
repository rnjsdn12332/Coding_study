from collections import deque
s="KKACB"
s=list(s)
s.sort()
q=deque(s)
sum_num=0
for i in s :
    if not i.isalpha() :
        i=int(i)
        sum_num+=i
        q.popleft()
    else :
        break

print("".join(q)+str(sum_num))