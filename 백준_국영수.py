n=int(input())
array=[]


for _ in range(n) :
    array.append(input().split())
    
array.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[2]), x[0]))

for temp in array :
    print(temp[0])
