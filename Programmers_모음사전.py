num=0
def solution(word):
    arr = ["A", "E", "I", "O", "U"]
    answer = dict() 


    def dfs(c):
        global num 
        answer[c] = num 
        num += 1
        if len(c) == 5:
            return 
        for char in arr:
            dfs(c + char) 

    dfs("")

    return answer[word]
