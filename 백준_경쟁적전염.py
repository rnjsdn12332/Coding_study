from collections import deque

n, k = map(int, input().split())
graph=[]
data=[]
for i in range(n) :
    graph.append(list(map(int, input().split())))
    for j in range(n) :
        if graph[i][j]!=0 :
            data.append((graph[i][j],0,i,j))
data.sort()
q=deque(data)

s, x, y= map(int, input().split())

dx=[-1,0,1,0]
dy=[0,1,0,-1]




            
while q :
    number, time, xx, yy=q.popleft()
    if time==s :
        break
    for i in range(4) :
        nx=xx+dx[i]
        ny=yy+dy[i]
        if nx>=0 and ny>=0 and nx<n and ny<n :
            if graph[nx][ny]==0 :
                graph[nx][ny]=number
                q.append((number, time+1, nx, ny))
        
print(graph[x-1][y-1])

