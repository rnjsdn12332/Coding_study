#게임개발
#현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 갈곳을 정함
#캐릭터의 바로 왼쪽 방향에 아직 가보지 않은칸이 존재 ->왼쪽 방향으로 회전한 다음 왼쪽으로 한칸 전진, 있다면 왼쪽 방향으로만 회전
#만약 네 방향 모두 가본칸이거나 바다로 되어있다면 바라보는 방향을 유지한 채 한칸 뒤로 가고 1단계로 돌아감. 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없으면 움직임을 멈춤

n, m=map(int,input().split())
x,y,d=map(int, input().split())

#맵 정보 입력해 리스트에 저장
map_list=[]
for _ in range(n):
        row=list(map(int,input().split()))
        map_list.append(row)
map_list[x][y]=1

def rotation() :
    global d
    d-=1
    if d==-1 :
        d=3

dx=[-1,0,1,0]
dy=[0,1,0,-1]
#시뮬레이션 시작

cnt=1
rotation_cnt=0
while True : 
    rotation()
    nx=x+dx[d]
    ny=y+dy[d]

    #회전한 이후 정면에 가보지 않은 칸이 있는 경우
    if map_list[nx][ny]==0 :
        map_list[nx][ny]=1
        x=nx
        y=ny
        cnt+=1
        rotation_cnt=0
        continue
    else :
        rotation_cnt+=1
    
    #네 방향 모두 갈 곳이 없을 경우
    if rotation_cnt==4 :
        nx=x-dx[d]
        ny=y-dy[d]
        if map_list[nx][ny]==0 :
            x=nx
            y=ny
        #뒤가 바다일 경우 탈출
        else :
            break
        rotation_cnt=0

print(cnt)
