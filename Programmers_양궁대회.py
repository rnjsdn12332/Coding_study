from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_sub = -1 
    
    for comb in combinations_with_replacement(range(11), n):
        info_l = [0] * 11

        for i in comb:
            info_l[10 - i] += 1
            
        apeach, lion = 0, 0
        for idx in range(11):
            if info[idx] == info_l[idx] == 0: 
                continue
            elif info[idx] >= info_l[idx]:  
                apeach += 10 - idx
            else: 
                lion += 10 - idx

        if lion > apeach: 
            sub = lion - apeach  
            if sub > max_sub: 
                max_sub = sub
                answer = info_l
    return answer
