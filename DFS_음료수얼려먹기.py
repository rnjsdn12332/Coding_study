
#n, m, map_list 입력 및 저장

n, m =map(int, input().split())
map_list=[]
for _ in range(n) :
    map_list.append(list(map(int, input())))


#연결된 상하좌우 노드 모두 방문
def dfs(x, y) :
    #특정 노드가 범위를 넘어서면 False 처리
    if x<0 or y<0 or x>=n or y>=m :
        return False
    #특정 노드가 0일 경우
    if map_list[x][y] == 0 :
        #방문 처리
        map_list[x][y]=1
        #상하좌우 탐색
        dfs(x-1,y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

cnt=0
for i in range(n) :
    for j in range(m) :
        # 현재 노트에 대한 깊이 우선 탐색
        if dfs(i, j) == True :
            cnt+=1

print(cnt)
