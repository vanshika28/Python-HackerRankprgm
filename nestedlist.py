reportcard=[]
marks =[]
n=int(input())
for i in range(0,n):
    a=input()
    b=float(input())
    reportcard.append([a,b])
    marks.append(b)
k=sorted(list(set(marks)))[1]
for a,b in sorted(reportcard):
    if b==k:
        print(a)

