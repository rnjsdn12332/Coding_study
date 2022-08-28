food_times=[3,1,2]
k=5
time=0
num=0
while time<k :
    for i in range(len(food_times)) :
        if food_times[i]!=0:
            food_times[i]-=1
            time+=1
            num=i%(len(food_times)-1)+1

if food_times.count(0)==len(food_times) :
    print(-1)
else : 
    print(num)