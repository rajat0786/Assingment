#ASSIGNMENT 11


#Q1


class Animal:
    def animal_attribute(self):
        print("tiger has 4 legs :-)")
class Tiger(Animal):
    def specs(self):
        print("Tiger is carnivorous")
d=Tiger()
d.animal_attribute()
d.specs()


#Q2

#1 A B
#2 A B


#Q3


class Cop:
    def __init__(self,name,age,work__experience,designation):
        self.name=name
        self.age=age
        self.work__experience=work__experience
        self.designation=designation
    def display(self):
        print("before update")
        print("name=",self.name)
        print("age=",self.age)
        print("work experience=",self.work__experience)
        print("designation=",self.designation)
    def __update__(self,name,age,work__experience,designation):
        self.name = name
        self.age = age
        self.work__experience = work__experience
        self.designation = dessignation
class Mission(Cop):
    def add_mission_detail(self,name,age,work__experience,designation):
        print("updated cop details are")
        print("name=", end="")
        self.name = name
        print(name)
        print("age=", end="")
        self.age = age
        print(age)
        print("work__experience=", end="")
        self.work__experience = work__experience
        print(work__experience)
        print("designation=", end="")
        self.designation = designation
        print(designation)

x=Mission("rajat",18,10,"manager")
name=input("enter name")
age=int(input("enter age"))
work__experience=(input("enter work experience"))
designation=input("designation")
x.display()


y=Mission(name,age,work__experience,designation)
y.add_mission_detail(name,age,work__experience,designation)







#Q4


class shape:
    def __init__(self,lenght,breadth):
        self.lenght=lenght
        self.breadth=breadth
        def area(self):
            arae = self.lenght * self.breadth
            print(area)
class rectangle(shape):
    def area(self):
        area = self.lenght * self.breadth
        print("area of rectangle is=", end="")
        print(area)
class square(shape):
    def area(self):
        area = self.lenght * self.breadth
        print("area of square is=",end="")
        print(area)
a=rectangle(10,20)
b=square(10,10)
a.area()
b.area()
