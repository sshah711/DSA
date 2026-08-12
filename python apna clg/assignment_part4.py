# Q1. BankAccount — Classes & Objects
class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return "Amount deposited successfully"
        return "Invalid amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return "Amount withdrawn successfully"
        return "Insufficient balance"

    def check_balance(self):
        return self.balance


account = BankAccount("ACC101", "Sakshi", 10000)

print(account.account_number, account.owner_name, account.balance)
print(account.deposit(2000))
print(account.withdraw(3000))
print(account.check_balance())

# Q2. Book — Reviews


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.list_of_reviews = []

    def add_new_review(self, new_review):
        self.list_of_reviews.append(new_review)

    def count_review(self):
        return len(self.list_of_reviews)

    def display_reviews(self):
        for review in self.list_of_reviews:
            print(review)


book = Book("Python Programming", "sakshi")

book.add_new_review("Very useful book")
book.add_new_review("Easy to understand")
book.add_new_review("Good for beginners")

print(book.count_review())

book.display_reviews()


# Q3. Student — Encapsulation
class Student:
    def __init__(self, name, roll_no, marks):
        self._name = ""
        self._roll_no = 0
        self._marks = 0

        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if name.strip() != "":
            self._name = name
        else:
            print("Name cannot be empty")

    def get_roll_no(self):
        return self._roll_no

    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self._roll_no = roll_no
        else:
            print("Roll number must be between 1 and 100")

    def get_marks(self):
        return self._marks

    def set_marks(self, marks):
        if marks >= 0:
            self._marks = marks
        else:
            print("Marks cannot be negative")


student = Student("Sakshi", 25, 85)

print(student.get_name())
print(student.get_roll_no())
print(student.get_marks())

# Q4. Shape — Function Overriding

import math


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r


class Rect(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w


class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return (self.h * self.b) / 2


s = Shape()
c = Circle(10)
r = Rect(2, 3)
t = Triangle(2, 5)
print(c.area())
print(r.area())
print(t.area())

# Q5. Vehicle — Inheritance


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc


car = Car("Toyota", "Fortuner", 7)

bike = Bike("Honda", "CBR", 500)

print(car.brand)
print(car.model)
print(car.seats)

print(bike.brand)
print(bike.model)
print(bike.engine_cc)

# Q6. Employee — Abstraction
from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class Intern:
    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend

class FullTimeEmployee:
    def __init__(self, monthlySalary):
        self.monthlySalary = monthlySalary

    def calculate_salary(self):
        return self.monthlySalary

class ContractEmployee:
    def __init__(self, hours,rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours*self.rate


intern = Intern(15000)
full_time = FullTimeEmployee(60000)
contract = ContractEmployee(160, 100)

print(intern.calculate_salary())
print(full_time.calculate_salary())
print(contract.calculate_salary())

# Q7. Person — Constructor Overloading

class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)

        if self.age is not None:
            print("Age:", self.age)

        if self.address is not None:
            print("Address:", self.address)


person1 = Person("Sakshi")

person2 = Person("Rahul", 25)

person3 = Person("Amit", 30, "Ahmedabad")

person1.display()
person2.display()
person3.display()

# Q8. Player — Class & Instance Attributes

class Player:
    player_count=0
    def __init__(self,name,level):
        self.name=name
        self.level=level

        Player.player_count+=1

player1 = Player("Sakshi", 10)
player2 = Player("Rahul", 15)
player3 = Player("Amit", 20)

print(player1.name)
print(player1.level)

print(Player.player_count)

# Q9. Multiple Inheritance — Bear
class Herbivore:
    def eat_plants(self):
        print("Eats plants")


class Carnivore:
    def eat_meat(self):
        print("Eats meat")


class Omnivore:
    def eat_both(self):
        print("Eats plants and meat")


class Bear(Herbivore, Carnivore, Omnivore):
    def show(self):
        print("Bear is an omnivore")


bear = Bear()

bear.show()
bear.eat_plants()
bear.eat_meat()
bear.eat_both()

# Q10. Mini Project — OOP Chat System
from datetime import datetime

class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username


class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text
        self.time = datetime.now()

    def display(self):
        print(
            f"[{self.time.strftime('%H:%M:%S')}] "
            f"{self.sender}: {self.text}"
        )


class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def join(self, user):
        if user not in self.users:
            self.users.append(user)
            print(user.username, "joined the chatroom")

    def leave(self, user):
        if user in self.users:
            self.users.remove(user)
            print(user.username, "left the chatroom")

    def send_message(self, user, text):
        if user in self.users:
            message = Message(user.username, text)
            self.messages.append(message)
        else:
            print("User is not in the chatroom")

    def view_history(self):
        for message in self.messages:
            message.display()


user1 = User("Sakshi")
user2 = User("Rahul")

chatroom = ChatRoom("Python Group")

chatroom.join(user1)
chatroom.join(user2)

chatroom.send_message(user1, "Hello everyone!")
chatroom.send_message(user2, "Hello Sakshi!")

chatroom.view_history()

chatroom.leave(user2)