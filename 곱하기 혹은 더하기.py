data=str(input())
sumv=0
for i in data :
    temp=int(i)
    if sumv==0 or sumv==1 or temp==0 or temp==1 :
        sumv=sumv+temp
    else :
        sumv*=temp

print(sumv)