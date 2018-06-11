ASSIGNMENT 5

q1

y=int(input("enter a year"))
if(y%4==0):
    print("%d is a leap year"%(y))
else:
   print("%d is not a leap year"%(y))



Q2

x=int(input("enter lenght"))
y=int(input("enter breadth"))
if(x==y):
    print("it is a square")
else:
    print("it is a rectangle")



Q3

x=int(input("enter age of first person"))
y=int(input("enter age of second person"))
z=int(input("enter age of third person"))
if (x>y and x>z):
    print("%d is the oldest"%(x))
elif (y>x and y>z):
    print("%d is the oldest"%(y))
elif (z>x and z>y):
    print("%d is the oldest"%(z))
else:
    print("all have same age")


if (x<y and x<z):
    print("%d is the youngest"%(x))
elif (y<x and y<z):
    print("%d is the youngest"%(y))
elif (z<x and z<y):
    print("%d is the youngest"%(z))
else:
    print("all have same age")



Q4

point=int(input("enter the points"))
if(point>1 and point<=50):
    print("sorry! no prize this time")
elif(point>50 and point<=150):
    print("congratilations! you won a wooden dog")
elif(point>150 and point<=180):
    print("congratulations! you won a book")
elif(point>180 and point<=200):
    print("congratulations! you won chocolates")
else:
    print("sorry! no prize this time")


Q5

s=int(input("enetr quantity. one unit will cost 100 rupees"))
r=s*100
if(r>1000):
    p=r-.1*r
    print("total cost is  %d rupees"%(p))
else:
    print("total cost is %d rupees"%(r))
