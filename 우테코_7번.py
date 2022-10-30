user="mrko"
friends=[ ["donut", "andole"], ["donut", "jun"], ["donut", "mrko"], ["shakevan", "andole"], ["shakevan", "jun"], ["shakevan", "mrko"] ]
visits=["bedi", "bedi", "donut", "bedi", "shakevan"]
answer=[]
#유저의 친구
userf=[]

#추천 점수 넣을 딕셔너리
dic=dict()

#유저의 친구 찾기
for a,b in friends :
    #둘중 한명이 사용자면 사용자 친구 넣는 배열에 나머지 한명 넣기
    if a==user :
        userf.append(b)
    elif b==user :
        userf.append(a)

#추천 점수 10점 넣기
for a,b in friends :
    #사용자 친구에 해당하는 사람이 있고, 상대방이 사용자가 아닌 다른 사람일 때 10점 추가
    if a in userf :
        if b!=user :
            #이미 사전에 이름이 등록되어있으면 +10점 추가
            if b in dic.keys() :
                dic[b]+=10
            #없다면 이름 등록하고 10점 부여
            else :
                dic[b]=10

    elif b in userf :
        if a!=user :
            if a in dic.keys() :
                dic[a]+=10
            else :
                dic[a]=10

#방문점수주기
for visit in visits :
    if visit in dic.keys():
        dic[visit]+=1
    else :
        dic[visit]=1


#정렬을 위한 리스트로 변환
result=list(dic.items())

print(result)

#정렬-점수순, 이름순 다중조건 부여하여 정렬
result=sorted(result,  key=lambda x : (-x[1], x[0]))

#결과 도출
for res in result :
    #결과 배열에 5명 이하일 때
    if len(answer)<=5 :
        #사용자 친구이지 않을 경우 결과 배열에 추가
        if not res[0] in userf :
            answer.append(res[0])

print(answer)
