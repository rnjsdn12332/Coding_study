def solution(s):
    answer=[]
    array=[]
    #맨 처음과 마지막의 괄호 삭제
    s=s[1:-1]
    #주어진 집합을 이중 리스트로 저장
    for i, char in enumerate(s) :
        if char=="{" :
            idx=i+1
        elif char=="}" :
            array.append(s[idx:i].split(","))
    #이중 배열 안 배열의 길이 순으로 정렬
    array=sorted(array, key=lambda x:len(x))
    
    #answer에 삽입
    for i in array :
        for j in i :
            if not int(j) in answer :
                answer.append(int(j))
    return answer
