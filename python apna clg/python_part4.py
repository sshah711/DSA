# sum= lambda a,b:a+b
# a=int(input())
# b=int(input())
# print(sum(a,b))

# class and object
# class is a blueprint of object
# object is an instance of class


class Student:
    # name
    # age
    # grade
    subject = "python"


s1 = Student()
print(s1.subject)


# attributes and methods
# init method is a constructor which is called when an object is created
class Studentt:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    subject = "python"

    def get_grade(self):
        return self.grade


s1 = Studentt("sakshi", 20, "A")
s2 = Studentt("priya", 24, "C")
print(s1.subject)
print(s2.name, s2.age, s2.grade)
print(s2.get_grade())

# type of constructor
# default constructor and parameterized constructor
# multiple constructors are not allowed in python but we can achieve it using default arguments


class constrct:
    def __init__(self):
        print("default constructor")

    def __init__(self, name):
        print("parameterized constructor")
        self.name = name


s111 = constrct("sakshi")
print(s111.name)

# class and instance attributes'
# class attributes are belong to class so we can access through obj name or class name
# instance attributes are belong to object so here we can only access through obj name
# when we create both class and instance value with the same name at that time when we call through obj name at that time instance value will be printed
# when we create both class and instance value with the same name at that time when we call through class name at that time class value will be printed


class stu:
    cname = "asd"  # class atr
    sum = 5.4

    def __init__(self, name, cpi):
        self.name = name  # instance atr
        self.cpi = cpi
        self.sum = 5.44


ss1 = stu("sak", 9)  # object
print(ss1.cname)  # through obj name
print(stu.cname)  # through class name
print(ss1.name, ss1.cpi)
print(stu.sum)
print(ss1.sum)


# methods instance,class,static

# instance methods -1st parameter is self
# -access the class and instance attr

# class methods -1st parameter is cls
# -access the class attr only -
#  decorator => @classmethod - change the behaviour of method
# class method obj as well as cclass ke name se b call ho skti h


# static methods - no compulsory parameter
# no self or class param
# they not access instance or class attr
# @staticmethod
class laptop:
    storage_type = "ssd"

    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"laptop has {cls.storage_type}")

    def get_info(self):  # instance methods -access the class and instance attr
        print(f"laptop has {self.ram} ram and {self.storage} {self.storage_type}")

    @staticmethod
    def cal_discount(p, d):
        finalp = p - (d * p / 100)
        print(f"final price are {finalp}")


l1 = laptop("1gb", "11gb")
l2 = laptop("12gb", "16gb")

l1.get_info()
l2.get_info()
l2.get_storage_type()  # obj name se call
laptop.get_storage_type()  # class name se call
laptop.cal_discount(200, 3)  # class name se call
l1.cal_discount(200, 3)  # obj name se call


class products:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        products.count += 1

    def get_info(self):
        print(f"price of {self.name} is rs. {self.price}")

    @classmethod
    def get_count(cls):
        print(f"count is {cls.count}")


    @staticmethod
    def cal_discountt(p, d):
        finalprice = p - (p * d / 100)
        print(f"final price are {finalprice}")


p1 = products("aalu", 20)
p11 = products("lu", 10)
p111 = products("matar", 50)
p1111 = products("gajar", 40)
p1.get_info()
products.get_count()
p1.cal_discountt(p1.price, 10)


# encapsulation- data hiding & binding - methods and attr are bind together  
# attr- public-access claas inside or outside , private- access only inside the class, protected- access inside the class as well as sub class(inheritance)

class socialmedia:
    def __init__(self, name, followers, platform,reels):
        self.name=name #by default public
        self.followers=followers
        self._platform=platform #atr ke aage _ lga diya so now its become protected attr
        self.__reels=reels #atr ke aage __ lga diya so now its become private attr 
        # data mangling

    def get_reels(self):
        return self.__reels
    def set_reels(self,newreel):
            self.__reels=newreel

soc1=socialmedia("sakshi",350,"instagram",22)
soc1.set_reels(11)
print(soc1.name,soc1.followers,soc1._platform,soc1.get_reels())
print(soc1.name,soc1._platform,soc1._socialmedia__reels)  #objname._classname__private attr --- is tarah se b hum private attr ko access kr skte h


# inheritance - ek class ki property ko dusre class me use krna
# reusing atrr and methods from parent class(base class) to child class(derived class)
# 3type of inheritance are there: 1) single level I- one parent child 
# 2)multilevel I- parent ke niche child uske b niche ek or child - example: employee->adminstaff->account
# 3)multiple I- multiple parent ki property child me hogi - example: teacher, student are parent & TA are chlid so that IA class ke pass thodi student class ki property hogi or thodi teacher class ki 


class employess:   #patent class
    # def __init__(self,stime,etime):
        # self.name=name
        stime="10am"
        etime="5pm"

        def change_time(self,new_etime):
            self.etime=new_etime

    # [ multilevel I
class teacher(employess):     #child class
    def __init__(self,sub):
        self.sub=sub

class admin(employess):          #child class
    def __init__(self,role):
        self.role=role

class account(admin):
    def __init__(self, salary,role):
        super().__init__(role)
        self.salary=salary
# ]


# [ multiple I
class teachers():     #parent class
    def __init__(self,sub):
        self.sub=sub

class student():            #parent class
    def __init__(self,year):
        self.year=year

class TA(teachers,student):          #child class
    def __init__(self,sub,year,name):
        super().__init__(sub)
        student.__init__(self,year)
        self.name=name

# ]

# e1=employess("sakshi","10am","6pm")
ta1=TA("physics",2020,"shah sakshi")
print(ta1.name,ta1.year,ta1.sub)
t1=teacher("math")
t2=admin("manager")
t3=account(23000,"hod")
t1.change_time("2pm")
t2.change_time("3pm")
t3.change_time("9pm")
print(t1.sub,t1.stime,t1.etime)
print(t2.role,t2.stime,t2.etime)
print(t3.salary,t3.role,t3.etime)


# abstraction - hinding internal details and show only essential details - example: chatgpt ya claude h to usme hum direct answer dekh pate h backend me konsa algo run ho rha h ya konsa data akha ja rha h we don't know
# diff btn encalsulation data hiding and abstraction is that wha pr hum data ko hide krte h sirf or yha pr humko kon se data ko hide krna h as well as konse data ko show krna h wo dikhate h
# abstract class - blueprint for other classes
# not implement the method of abstract class but inhe hum inherit kr ke dusre(child) class me implement krte h
from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def makesound(self):     #implementiation details ko hide kr rhe h
        pass


class cat(animal):
    def makesound(self):
        print("meow")


class cow(animal):
    def makesound(self):
        print("moo")

c1=cat()
c1.makesound()
c2=cow()
c2.makesound()


# polymorphism- many forms - multiple functions with same name & diff implementation
# operator overloading- ex: + add, concate
print(1+2, "h"+"ii")
# function overriding (inheritance)- redefining parent class's fuc in child class-- parent - fun() same child- fun()
# duck typing-- walks like a duck & quacks like a duck 

class Emp:
    def get_deg(self):
        print("deg is emp")
class Teacher(Emp):
    def get_deg(self):   #override the same function 
        print("deg is teacher")

t=Teacher()
t=Emp()
t.get_deg()

# dono class ek dusre se relavent nhi h koi kisi ki subclass nhi h lekin dono ke andar same kam krne vala function h to ise hum duck typing kehte h
class Teacher1():
    def get_deg(self):   #duck typing the same function 
        print("deg is tea")

class Accountant():
    def get_deg(self):   #duck typing the same function 
        print("deg is actnt")

t=Teacher1()
t.get_deg()
t=Accountant()
t.get_deg()