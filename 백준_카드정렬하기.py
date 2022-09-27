import heapq
n=int(input())
card_arr=[]
for i in range(n) :
    heapq.heappush(card_arr,int(input()))

answer=0
while len(card_arr)>1 :
    first=heapq.heappop(card_arr)
    sec=heapq.heappop(card_arr)
    card_cnt=first+sec
    answer+=card_cnt
    heapq.heappush(card_arr, card_cnt)
print(answer)

