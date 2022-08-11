#첫째줄에 공간의 크기를 나타내는 n
#둘째줄에 여행가 a가 이동할 계획서 내용이 주어짐(1<=이동횟수<=100)
#첫째줄에 여행가 a가 최종적으로 도착할 지점의 좌표(x, y)를 공백으로 구분하여 출력한다.

n=int(input())
plans=input().split(" ")

x=1
y=1
nx=0
nx=0
ny_list=[1,-1,0,0]
nx_list=[0,0,-1,1]
maps=["R","L","U","D"]

for plan in plans :
    for i in range(len(maps)) :
        if plan==maps[i] :
            nx=x+nx_list[i]
            ny=y+ny_list[i]
    if nx<=0 or ny<=0 or nx>n or ny>n:
        continue
    x=nx
    y=ny
print(x, y)
            
    

