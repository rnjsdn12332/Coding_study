'''
#내 풀이ㅣ
#입력
s=input()
#s의 첫번째 문자 저장
temp=s[0]
#축소 저장할 배열 초기화
word_list=[]
for char in range(1,len(s)) :
    #기존 문자와 현재 문자가 다를때 wordlist에 저장하고 현재 문자로 값 변환
    if s[char]!=temp :
        word_list.append(temp)
        temp=s[char]

#0의 횟수와 1의 횟수의 최솟값
answer=min(word_list.count("0"), word_list.count("1"))
print(answer)

'''
#책에서의 풀이

data=input()
count0=0 #전부 0으로 바꾸는 횟수
count1=0 #전부 1로 바꾸는 함수

#첫번째 문자에 대한 처리
if data[0]=="1" :
    count0+=1
else :
    count1+=1

for i in range(len(data)-1) :
    if data[i+1]=="1" :
        count0+=1
    elif data[i+1] == "0" :
        count1+=1

answer=min(count0, count1)