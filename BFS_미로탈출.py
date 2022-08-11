#nxm 크기의 직사각형
#0으로 간 곳은 못 가고 1로 된 부분만 갈 수있음
#(1,1)부터 시작했을때 (n, m)으로 이동하는 경로의 최소 칸의 갯수

from collections import deque

n, m = map(int, input().split())
map_list=[]

for _ in range(n) :
    map_list.append(list(map(int, input())))

dx=[-1, 1, 0, 0]
dy=[0,0,-1,1]

def bfs(x, y) :
    queue=deque()
    queue.append((x,y))
    #queue 가 빌때까지 반복
    while queue :
        #방문한 노드 queue에서 제거
        x,y=queue.popleft()

        for i in range(4) :
            nx=x+dx[i]
            ny=y+dy[i]
            #범위에서 벗어나면 무시
            if nx<0 or ny<0 or nx>=n or ny>=m :
                continue
            #0인 경우 무시
            if map_list[nx][ny]==0 :
                continue
            #해당 노드를 처음 방문했을 경우 최단 거리 기록
            if map_list[nx][ny] == 1 :
                map_list[nx][ny]=map_list[x][y]+1
                queue.append((nx, ny))
                
    return map_list[n-1][m-1]

print(bfs(0,0))


