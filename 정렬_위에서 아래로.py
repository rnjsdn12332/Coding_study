#위에서 아래로
n=input()
num_list=[]
for i in range(int(n)):
    num_list.append(int(input()))
    print(num_list[i])
array=sorted(num_list, reverse=True)
print(array)