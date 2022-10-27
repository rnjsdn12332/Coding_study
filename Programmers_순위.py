
def DFS(x,graph):
    visited[x] = True
    for i in graph[x]:
        if visited[i] == False:
            DFS(i,graph)
def solution(n, results):
    global visited
    visited = [False for _ in range(n)]
    answer = 0
    graph = [[] for _ in range(n)]
    for a,b in results:
        graph[a-1].append(b-1)

    score = []
    for i in range(n):
        DFS(i,graph)
        score.append(visited)
        visited = [False for _ in range(n)]

    new_score = []
    
    for j in range(len(score)):
        new_visited = [False for _ in range(n)]    
        for i in range(len(score)):
            if score[i][j] == True or score[j][i] == True:
                new_visited[i] = True


        new_score.append(new_visited)
    for i in new_score:
        if sum(i) == n:
            answer += 1
    return answer
