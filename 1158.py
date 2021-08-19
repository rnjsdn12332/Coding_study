c, n=map(int, input().split())
josephus = [i for i in range(1, c+1)]

result=[]
seqNo=n-1

while len(josephus) :
    if seqNo>=len(josephus) :
        seqNo=seqNo % len(josephus)
    else :
        result.append(str(josephus.pop(seqNo)))
        seqNo +=(n-1)

print("<",", ".join(result),">",sep='')
