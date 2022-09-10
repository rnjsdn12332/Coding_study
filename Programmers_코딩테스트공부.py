def solution(alp, cop, problems):
    answer = 0
    target_alp=0
    target_cop=0
    for i in range(len(problems)) :
        target_alp=max(problems[i][0], target_alp)
        target_cop=max(problems[i][1], target_cop)
    
    alp=min(alp, target_alp)
    cop=min(cop, target_cop)
    
    inf=float('inf')
    dp=[[inf]*(target_cop+1) for _ in range(target_alp+1)]
    dp[alp][cop]=0
    for x in range(alp, target_alp+1) :
        for y in range(cop, target_cop+1) :
            if x+1<=target_alp :
                dp[x+1][y]=min(dp[x+1][y], dp[x][y]+1)
                
            if y+1<=target_cop :
                dp[x][y+1]=min(dp[x][y+1], dp[x][y]+1)
                
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems :
                if x >=alp_req and y>=cop_req :
                    next_alp, next_cop=min(target_alp, x+alp_rwd), min(target_cop, y+cop_rwd)
                    dp[next_alp][next_cop]=min(dp[next_alp][next_cop], dp[x][y]+cost)

        
        
        
    return dp[-1][-1]
