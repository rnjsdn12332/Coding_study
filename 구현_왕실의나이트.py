# 첫째 줄에 8x8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력됨. 
# 입력 문자는 a1처럼 열과행으로 이뤄짐
# 첫째줄에 나이트가 이동할 수 있는 경우의 수를 출력

start=str(input())
start_x=start[0]
alpha=["a","b","c","d","e","f","g","h"]
x=int(alpha.index(start_x)+1)
y=int(start[1])
method_list=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
cnt=0
for method in method_list :
    print(method)
    nx=x+method[0]
    ny=y+method[1]
    if nx<1 or ny<1 or nx>8 or ny>8 :
        continue
    else :
        cnt+=1
print(cnt)