n, m =map(int, input().split())
print(n,m)
map_list=[]
for _ in range(n) :
    map_list.append(list(map(int, input())))



def dfs(x, y) :
    if x<0 or y<0 or x>=n or y>=m :
        return False
    if map_list[x][y] == 0 :
        map_list[x][y]=1
        dfs(x-1,y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

cnt=0
for i in range(n) :
    for j in range(m) :
        if dfs(i, j) == True :
            cnt+=1

print(cnt)
