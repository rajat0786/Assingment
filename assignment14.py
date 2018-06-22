'''

#Q1
f=open("file.txt",encoding="utf8")
a=(f.readlines())
a.reverse()
n=int(input("enter number of lines u want to print"))
for i in range(0,n):
    print(a[i])
f.close()
'''

#Q2
'''
a="kill"
f=open("file4.txt","r")
k=f.read()
m=k.split()
print(k.count(a))
'''
#Q3
'''
f=open("file.txt",encoding="utf8")
a=(f.readlines())
c=open("file2.txt","w")
c.writelines(a)
'''

#Q4
'''
i=0
f=open("file2.txt",encoding="utf8")
a=(f.readlines())
b=open("file4.txt",encoding="utf8")
c=(b.readlines())
d= open("file3.txt","w")
for i,j in zip(a,c):
    d.write(i+j)
f.close()
b.close()
d.close()
'''
#Q5
l=[]
j=[]
import json
import random
for i in range(0,10):
    l.append(random.randint(1,20))
f=open("file2.txt","w")
for t in l:
    h="".join(str(t))
    f.write(h+"\n")
f.close()
d=open("file2.txt","r")
a=d.read()
for x in a:
    if(x.isdigit()):
        str="".join(x)
        j.append(str)
j.sort()
c=open("file3.txt","w")
for k in j:
    c="".join(str(k))
    c.write(c+"\n")
