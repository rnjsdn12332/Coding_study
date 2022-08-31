from collections import deque

n=int(input())
graph=[[0]*n for _ in range(n)]

#뱀에 해당하는 좌표 1로 설정 시작은 0,0에서 시작함
graph[0][0]=1
#뱀에 해당하는 좌표 큐에 넣어주기
snake=deque([[0,0]])

#사과가 있는 곳 값 2로 설정
apple_cnt=int(input())
for _ in range(apple_cnt) :
     row, col=map(int, input().split())
     #1행1열이 (0,0)인 것처럼 -1한 인덱스에 넣어주는 것 유의
     graph[row-1][col-1]=2

d=int(input())

#시간과 방향 저장할 리스트 설정
dlist=[]
for _ in range(d) :
    t,order=input().split()
    dlist.append([int(t), order])
#초기준으로 정렬
dlist=sorted(dlist, key=lambda x : x[0])
dlist=deque(dlist)
#시작 시간과 시작 좌표 초기화
time=0
x=0
y=0

#상하좌우로 방향 바꿀 값 저장하는 리스트 설정
nd=[[0,1],[1,0],[0,-1],[-1,0]]

#초기는 오른쪽으로 움직임
direct=0

while True :
    time+=1
    
    #현재 시간의 방향대로 x와 y 좌표 이동
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
    	#꼬리 자르기
        sx, sy=snake.popleft()
        graph[sx][sy]=0
        #해당 좌표 뱀으로 설정
        graph[x][y]=1
        snake.append([x,y])
    #아직 처리하지 못한 방향 전환 명령이 있을 때
    if dlist:
        if time in dlist[0] :
            t, o=dlist.popleft()
            #오른쪽으로 회전
            if o=="D":
                direct+=1
            #왼쪽으로 회전
            elif o=="L" :
                direct-=1
    #dlist의 범위를 넘어서면 director 0으로 초기화
    if direct>=4 or direct<=-4 :
        direct=0

print(time)
