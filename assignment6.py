ASSIGNMENT 6


Q1

i=0
b=[]
while(i<10):
    a=int(input("enter a number"))
    b.append(a)
    i=i+1
for i in b:
    print(i)



Q2


while(True):
    print("infinite")

Q3


i=0
b=[]
c=[]
while(i<10):
    a=int(input("enter a number"))
    b.append(a)
    i=i+1
    d=i*i0
    c.append(d)
print("before square")
print(b)
print("after square")
print(c)



Q4


i=0
l=[1,2,"abc",2.0]
a=[]
b=[]
c=[]
for i in l:

    if (type(i)==int):
        a.append(i)
    elif (type(i)==str):
        b.append(i)
    else:
        c.append(i)
print(a)
print(b)
print(c)



Q5


even=[]
odd=[]
for i in range(1,101):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)



Q6


n=4
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print("\r")



Q7



d={'name':'rajat','age':18}
for i in d:
    print(i,d[i])



Q8

i=0
c=[]
while(i<5):
    a=int(input("enter number"))
    c.append(a)
    i=i+1
a=int(input("enter number to be searched"))
for i in c:
        if(a==i):
            c.remove(i)
print(c)