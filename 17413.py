import sys
s = list(sys.stdin.readline().rstrip())

n = 0
start = 0

while n < len(s):
    if s[n] == "<":       
        n += 1 
        while s[n] != ">":      
            n += 1 
        n += 1               
    elif s[n].isalnum(): 
        start = n
        while n < len(s) and s[n].isalnum():
            n+=1
        tmp = s[start:n] 
        tmp.reverse()       
        s[start:n] = tmp
    else:                   
        n+=1                

print("".join(s))
