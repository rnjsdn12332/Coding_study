n=int(input())
array=[]
for _ in range(n) :
    name, score=input().split()
    array.append((name, int(score)))


array_sort=sorted(array, key=lambda array : array[1])

for i in range(len(array)) :
    print(array_sort[i][0], end=" ")