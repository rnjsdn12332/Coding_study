from collections import defaultdict
def solution(n, paths, gates, summits):
    graph=defaultdict(list)
    summits.sort()
    check=set(summits)
    for start, end, cost in paths :
        graph[start].append((end, cost))
        graph[end].append((start, cost))
    
    intensity=[1e9]*(n+1)
    stack=gates
    
    for gate in gates :
        intensity[gate]=0
    
    while stack :
        target=set()
        
        while stack :
            now=stack.pop()
            for next_, cost in graph[now] :
                max_time=max(intensity[now], cost)
                
                if intensity[next_]>max_time :
                    intensity[next_]=max_time
                    
                    if next_ not in check :
                        target.add(next_)
        stack=list(target)
    
    
    return min([[summit, intensity[summit]] for summit in summits], key=lambda x: (x[1], x[0]))
