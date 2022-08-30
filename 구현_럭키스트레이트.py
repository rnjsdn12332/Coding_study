n=input()
score_list=[int(i) for i in n]
pivot=int(len(score_list)/2)
left=score_list[:pivot]
right=score_list[pivot:]
if sum(left)==sum(right):
    print("LUCKY")
else :
    print("READY")
