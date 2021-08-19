import sys
input=sys.stdin.readline

n=int(input())
for i in range(n) :
    sentence=list(input().strip().split())
    new=[None]*len(sentence)
    for j in range(len(sentence)) :
        word=[]
        for p in sentence[j] :
            word.insert(0, p)

        new[j]=''.join(word)
    print(' '.join(new))






