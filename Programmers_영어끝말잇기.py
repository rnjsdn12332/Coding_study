def solution(n, words):
    answer = []
    #사람 별 단어 횟수 체크하는 배열
    array=[0 for _ in range(n)]
    
    #단어별 사람번호 체크 사전
    word_dict=dict([(words[i], 0) for i in range(len(words))])
    
    
    for w in range(len(words)) :
        #처음 말하는 단어일 경우
        if word_dict[words[w]]==0 :
            #사람 번호 체크
            word_dict[words[w]]=w%n+1
            #사람 번호 별 횟수 카운트 
            array[w%n]+=1
        else : #이미 전에 말했던 단어일 경우
            
            return [w%n+1, array[w%n]+1]
        
        
        if w>=1 :
            #전 단어의 끝과 지금 단어의 처음이 같지 않을 경우
            if words[w-1][-1]!=words[w][0] :
                return [w%n+1, array[w%n]]
    # 아무도 틀리지 않을 때 [0,0] 반환
    return [0,0]
