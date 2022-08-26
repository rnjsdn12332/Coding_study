#왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자사이에 x와 +을 넣어 최대값을 만드는 
data=str(input())
sumv=0
for i in data :
    temp=int(i)
    if sumv==0 or sumv==1 or temp==0 or temp==1 :
        sumv=sumv+temp
    else :
        sumv*=temp

print(sumv)
