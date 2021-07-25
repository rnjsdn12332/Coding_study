import sys


class Stack1 :
    def __init__(self, size) :
        self.arr=[None]*size
        self.last_index=0

    def push(self, value):
        self.arr[self.last_index]=value
        self.last_index+=1

    def pop(self):
        if self.last_index==0:
            print(-1)
        else :
            self.last_index=self.last_index-1
            print(self.arr[self.last_index])

    def size(self):
        print(self.last_index)

    def empty(self):
        if self.last_index==0:
            print(1)
        else :
            print(0)
    def top(self):
        if self.last_index == 0:
            print(-1)
        else :

            print(self.arr[self.last_index-1])
input=sys.stdin.readline
s=int(input())

st=Stack1(s)
for i in range(s) :
    quest=input().strip()
    if ' ' in quest :
        a, b=quest.split()
        if a=='push' :
            st.push(int(b))
    else :
        a=quest
        if a=='pop' :
            st.pop()
        elif a=='size' :
            st.size()
        elif a=='top' :
            st.top()
        elif a=='empty' :
            st.empty()

