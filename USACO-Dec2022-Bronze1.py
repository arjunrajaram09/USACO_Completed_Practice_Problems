#Competeitive Programming
b=int(input())
a=list((map(int,input().split())))
a.sort()

c=[]
for i in range(len(a)):
    d= (a[i])* (b-i)
    c.append(d)
e= c.index(max(c))
print(c[e],a[e])
