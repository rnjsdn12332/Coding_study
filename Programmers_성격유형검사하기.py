
def solution(survey, choices):
    answer = ''
    dic={'r':0,'t':0,'c':0,'f':0,'j':0,'m':0,'a':0,'n':0}
    def score(char, val) :
        up=char[0]
        down=char[1]
        if val==1 :
            dic[up]+=3
        elif val==2 :
            dic[up]+=2
        elif val==3:
            dic[up]+=1
        elif val==5 :
            dic[down]+=1
        elif val==6 :
            dic[down]+=2
        elif val==7 :
            dic[down]+=3
            
    
    for i in range(len(survey)) :
        score(survey[i].lower(),choices[i])
    
    if dic['r']>=dic['t'] :
        answer+="R"
    else :
        answer+="T"
    if dic['c']>=dic['f'] :
        answer+="C"
    else :
        answer+="F"
    if dic['j']>=dic['m'] :
        answer+='J'
    else :
        answer+='M'
    if dic['a']>=dic['n'] :
        answer+='A'
    else :
        answer+='N'
    
    return answer
