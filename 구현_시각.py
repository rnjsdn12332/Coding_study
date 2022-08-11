# 첫째줄에 정수 n이 입력된다(0<=n<=23)
#00시 00분 00초부터 n시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력

h=int(input())

count=0
for i in range(h+1) :
    for j in range(60) :
        for k in range(60) :
            if '3'in str(i)+str(j)+str(k) :
                count+=1