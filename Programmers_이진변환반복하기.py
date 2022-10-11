def solution(s):
    answer = [0,0]
    cnt=1
    def method(char) :
        zero_count=char.count("0")
        char=char.replace("0", "")
        
        trans_len=len(str(char))
        trans_bin=str(bin(trans_len))[2:]

        answer[1]+=zero_count
        answer[0]+=cnt   
        if trans_bin!="1" :
            method(trans_bin)
        else :
            return 
    method(s)
    
    return answer
