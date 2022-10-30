
from collections import deque
array=[ ["jm@email.com", "제이엠"], ["jason@email.com", "제이슨"], ["woniee@email.com", "워니"], ["mj@email.com", "엠제이"], ["nowm@email.com", "이제엠"] ]
q=deque(array)
answer=[]

#q가 빌떄까지
while q :
    #첫번째 들어온 사람 뽑음
    mail, name=q.popleft()

    #중복 확인용
    check=False

    #닉네임 이름 중에 한 글자씩 뽑기
    for i in range(1,len(name)) :

        #두 글자 조합 변수에 저장
        char=name[i-1:i+1]

        #나머지 큐 확인
        for _ in range(len(q)) :
            #하나 뽑기
            temp=q.popleft()
            m,n=temp
            #닉네임중 char이 포함되어있다면
            if char in n:
                #중복체크하고 answer에 메일주소 입력
                answer.append(m)
                check=True
            else :
                #중복이 안된다면 다시 큐에 삽입
                q.append(temp)

    #중복된 닉네임이 있었다면 answer에 삽입
    if check==True :
        answer.append(mail)

print(answer)

