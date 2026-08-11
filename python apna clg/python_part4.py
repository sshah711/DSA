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


