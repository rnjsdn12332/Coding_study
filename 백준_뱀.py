from collections import deque

n=int(input())
graph=[[0]*n for _ in range(n)]
graph[0][0]=1
snake_list=[[0,0]]
snake=deque(snake_list)
apple_cnt=int(input())
for _ in range(apple_cnt) :
    row, col=map(int, input().split())
    graph[row][col]=2


d=int(input())
dlist=[]
for _ in range(d) :
    t,order=input().split()
    dlist.append([int(t), order])

dlist=sorted(dlist, key=lambda x : x[0])
dlist=deque(dlist)
time=1
x=0
y=0
nd=[[1,0],[0,1],[-1,0],[0,-1]]
direct=0
while True :
    time+=1
    if dlist:
        if time in dlist[0] :
            t, o=dlist.popleft()
            if o=="D":
                direct+=1
                
            elif o=="L" :
                direct-=1
    if direct>=4 or direct<=-4 :
        direct=0
    nx=nd[direct][0]
    ny=nd[direct][1]

    x=x+nx
    y=y+ny
    #x와 y가 범위를 벗어날 때, 해당 위치가 뱀일때
    if x<0 or y<0 or x>n-1 or y>n-1  or graph[x][y]==1:
        break
    #사과를 만났을 때
    if graph[x][y]==2 :
        graph[x][y]=1
        snake.append([x,y])
    #사과도 벽도 뱀도 아닐떄 
    elif graph[x][y]==0 :
        sx, sy=snake.popleft()
        graph[sx][sy]=0
        snake.append([x,y])
print(time)

