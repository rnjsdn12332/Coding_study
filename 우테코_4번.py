
#문자열 입력
s=input()
answer=""
#단어사전
word='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#입력된 문자 한 단어씩 확인하기 위한 반복문
for char in s :
    #띄어쓰기면 띄어쓰기 그대로 입력
    if char==" " :
        answer+=" "
    else :
        #대문자일경우
        if char.isupper() :
            #find함수로 글자가 있는 인덱스를 추출후 n에 저장
            n=word.find(char)
            #순서를 뒤집어 찾아준 글자를 입력
            answer+=word[-(n+1)]
        #소문자일경우
        else :
            #대문자로 변환한 후 순서를 찾아낸뒤
            n=word.find(char.upper())
            #다시 소문자로 변환해서 입력
            answer+=word[-(n+1)].lower()

print(answer)
