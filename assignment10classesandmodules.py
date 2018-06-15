ASSIGNMENT 10



Q1



class Circle:
    def __init__(self,radius):
        self.r=radius
    def area(self):
        area=3.14*r*r
        return area
    def circumference(self):
        circumference=2*3.14*r
        return circumference
r=int(input("enter a radius"))
y=Circle(r)
print("area of circle is",y.area())
print("circumference of circle is",y.circumference())



Q2




class Student:
    def __init__(self,a,b):
        self.name=a
        self.rollnumber=b
name=input("enter your name ")
rollnumber=int(input("enter your roll number"))
y=student(name,rollnumber)
print(y.name)
print(y.rollnumber)




Q3


class Temperature:
    def f__to__c(c):
        return (c-32)/1.8
    def c__to__f(d):
        return ((d*1.8)+32)
y=temperature.f__to__c(68)
print(y)
y=temperature.c__to__f(20)
print(y)



Q4



class MovieDetails:
    def __init__(self,a,b,c,d):

        self.movie_name=a
        self.artist_name=b
        self.year_of_releasing=c
        self.ratings=d

    def __update__(self,a,b,c,d):
        print("updated movie details are")
        print("movie name=", end="")
        self.movie_name=a
        print(a)
        print("artist name=", end="")
        self.artist_name=b
        print(b)
        print("year of releasing=", end="")
        self.year_of_releasing=c
        print(c)
        print("ratings=", end="")
        self.ratings=d
        print(d)


x=MovieDetails("Race 3","salman khan","2018","**")
print("movie name=",end="")
print(x.movie_name)
print("artist name=", end="")
print(x.artist_name)
print("year of releasing=", end="")
print(x.year_of_releasing)
print("ratings=", end="")
print(x.ratings)



movie_name=input("enter movie name")
artist_name=input("enter artist name")
year_of_releasing=(input("enter the year"))
ratings=input("rate the movie")
y=MovieDetails(movie_name,artist_name,year_of_releasing,ratings)
y.__update__(movie_name,artist_name,year_of_releasing,ratings)




Q5




class Expenditure:
    def __init__(self,expenditure,savings,total=0):
        self.e=expenditure
        self.s=savings
        self.t=0

    def display(self):
        print("total expenditure=",end="")
        print(self.e)
        print("total savings=",end="")
        print(self.s)
    def total__salary(self):
        self.t=self.e+self.s
    def display__salary(self):
        return self.t
n=int(input("enter the expenditure"))
m=int(input("enter savings"))
y=Expenditure(n,m)
y.display()
y.total__salary()
print("total salary=",end="")
print(y.display__salary())
