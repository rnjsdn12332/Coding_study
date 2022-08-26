def solution(n):
    answer = []
    graph=[]
    for i in range(n) :
        graph.append([0]*n)
    d=[(1,0),(0,1),(-1,-1)]
    x=-1
    y=0
    num=0
    i=0
    while  n >0 :
        for _ in range(n) :
            i+=1
            x=d[num%3][0]+x
            y=d[num%3][1]+y
            graph[x][y]=i
        n-=1
        num+=1
    
    for i in range(len(graph)) :
        for j in range(len(graph[i])) :
            if graph[i][j]!= 0 :
                answer.append(graph[i][j])
    return answer
