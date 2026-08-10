word = "i am sakshi shah"
print(word[: len(word)])
print(word[0:6])
print(word[-2:-1])
# word[2]='w'  # This will cause an error because strings are immutable in Python
# for ch in word:
#     print(ch)

# normal formatting
print("shah {}".format("sakshi"))
# index based formatting
print("shah {0} {1}".format("sakshi", "i am"))
# value based formatting
print("shah {name} {age}".format(name="sakshi", age=22))
# f-string formatting
print(f"hello {word} ")


# lists- mutable sequence of values
marks = [11, 22, 32, 3, 43.4, "ss", [1, 2, 3]]
print(type(marks))
print(marks[3])
marks[3] = 100
print(marks[1 : len(marks)])
print(marks[-3:])

marks.append(1000)
print(marks)

marks.insert(2, 2000)
print(marks)

marks.reverse()
print(marks)

marks.remove("ss")
marks.remove([1, 2, 3])
print(marks)

marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks)

# linear search
idx = 0
x = 11
# x=int(input("Enter the number to find index: "))
for i in marks:
    if i == x:
        print(f" Index of {x} is: {idx}")
        break
    idx += 1
    # print(i)


# tuples- immutable sequence of values
tup = (11, 22, 32, 223, 43.4, "ss", (1, 2, 3))
tup1 = (11, 22, 32, 223, 43)
print(type(tup))
print(tup)
print(len(tup))
print(tup[3 : len(tup)])
# tup[3]=100  # This will cause an error because tuples are immutable in Python

sum = 0
for i in tup1:
    sum += i
print(f"Sum of all elements in tuple is: {sum}")

tup2 = (11, 22, 22, 22, 43)

print(tup2.count(22))
print(tup2.index(22))  # index of first occurrence of 22 in tuple

# dictionaries- mutable, unordered sequence of key-value pairs
dict1 = {"name": "sakshi", "age": 22, "college": "apna clg"}
print(type(dict1))
print(dict1)

print(dict1["name"])

dict1["age"] = 23
print(dict1)

print(list(dict1.keys()))

print(tuple(dict1.values()))

print(dict1.items())

# accessing values for 2 ways one is using key and other is using get method ,
# the difference is that if key is not present in dictionary then using key will give error but using get method will return None
print(dict1["name"])
print(dict1.get("name"))

# updating values using key and using update method ,
# difference is that using key will update only one value but using update method we can update multiple values at once
dict1["age"] = 28
print(dict1)
dict1.update({"name": "sakshi shah", "age": 24})
print(dict1)

# sets- mutable, unordered collection of unique elements (no duplicates allowed)

set1 = {1, 2, 2, 2, 2, 6, 7, 8}
s = {11, 22, 33, 44, 55, 2, 1, 6}
print(set1)
print(len(set1))
print(type(set1))

set1.add(3)
print(set1)

set2 = set()
print(type(set2))

set1.remove(2)
print(set1)

print(set1.pop())

print(set1.union(s))

print(set1.intersection(s))

set1.clear()
print(set1)


# list of tuples
l1 = [
    ("sakshi", "math"),
    ("shah", "science"),
    ("apna clg", "maths"),
    ("prit", "programming"),
    ("pia", "programming"),
    ("sakshi", "english"),
    ("shah", "english"),
]

for i in l1:
    print(i[1])

# list all unique subjects from the list of tuples
subjects = set()
for name, subject in l1:
    subjects.add(subject)
print((subjects))

# list students who are learning programming
# students = []
for name, subject in l1:
    if subject == "english":
        # students.append(name)
        print(name)
# print(students)

# create dictionary student as key and subject as value from the list of tuples
distt = {}
for name, subject in l1:
    if distt.get(name) is None:
        distt.update({name: set()})
        distt[name].add(subject)
    else:
        distt[name].add(subject)
print(distt)


# assignments
# srting palindrom or not
str = input("Enter a string to check if it is palindrome or not: ")
# if str==str[::-1]:
rev = ""
for i in range(len(str) - 1, -1, -1):
    rev += str[i]
if str == rev:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome")

# list of int compute the avg of all num in list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sum(nums):
    s = 0
    for i in nums:
        s += i
    return s


avg = sum(nums) / len(nums)
print(f"Average of all numbers in the list is: {avg}")

# Input two lists of integers from the user. Merge them into one list and sort the result. Q3 Eg-, list1 = [1, 2, 7] list2 = [2, 4, 5] result = [1, 2, 3, 54, 5, 7]


l1 = [
    int(x) for x in input("Enter first list of integers separated by space: ").split()
]
l2 = [
    int(x) for x in input("Enter second list of integers separated by space: ").split()
]

l = l1 + l2
print(f"Merged list is: {l}")
l.sort()
print(f"Sorted merged list is: {l}")

# given a tuple of integers, create: A tuple of all even numbers and A tuple of all odd numbers
tup = (int(x) for x in input("Enter a tuple of integers separated by space: ").split())
even = ()
odd = ()
for i in tup:
    if i % 2 == 0:
        even += (i,)
    else:
        odd += (i,)
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")

# Create a dictionary where: • Keys = student names • Values = marks (integer) Write a menu-based program where user presses a key (ʼAʼ,‘Bʼ,‘Cʼ,‘Dʼ) depending on the operation they want to perform on the dictionary: 1. A - Add a student  2. B - Update marks  3. C - Search for a student  4. D - Display all students and marks
dict1 = {}
while True:
    print("Menu:")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    choice = input("Enter your choice: ")
    if choice == "A":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        dict1[name] = marks
        print(f"Student {name} added with marks {marks}")
    elif choice == "B":
        name = input("Enter student name to update marks: ")
        if name in dict1:
            marks = int(input("Enter new marks: "))
            dict1[name] = marks
            print(f"Marks for student {name} updated to {marks}")
        else:
            print(f"Student {name} not found")
    elif choice == "C":
        name = input("Enter student name to search: ")
        if name in dict1:
            print(f"Student {name} has marks {dict1[name]}")
        else:
            print(f"Student {name} not found")
    elif choice == "D":
        print("Students and their marks:")
        for name, marks in dict1.items():
            print(f"{name}: {marks}")
    else:
        print("Invalid choice. Please try again.")
        break


# Given a list of words: Q6 words = ["apple", "banana", "kiwi", "cherry", "mango"] Create a dictionary that maps each word to its length. Example: {"apple": 5, "banana": 6, "kiwi": 4, ...}
words = ["apple", "banana", "kiwi", "cherry", "mango"]
word_lengths = {}
for word in words:
    word_lengths[word] = len(word)
print(word_lengths)

# Write a program that takes a string from the user and prints the number of spaces in the string
s=input("Enter a string: ")
# print(f"space is: {s.count(' ')}")
sp=0
for i in s:
    if i==" ":
        sp+=1
print(f"Number of spaces in the string is: {sp}")

# Write a program to check whether two lists share no common elements. Q8
# share no common elements list1 =[1,2,3,4] list2 =[5,6,7,8]
# share common elements list1 =[1,2,3] list2 =[3,4][-usesets]

s1 = [int(x) for x in input("Enter first list of integers separated by space: ").split()]
s2 = [int(x) for x in input("Enter second list of integers separated by space: ").split()]
# if set(s1) & set(s2):
if set(s1).intersection(set(s2)):
    print("Lists share common elements")
else:
    print("Lists share no common elements")

# Given a list, print all elements that appear more than once in the list. [-use sets]
l = [int(x) for x in input("Enter a list of integers separated by space: ").split()]
seen = set()
duplicate = set()
print(f"list is: {set(l)}")
for x in l:
    if x in seen:
        duplicate.add(x)
    else:
        seen.add(x)
print(f"duplicate elements in the list are: {duplicate}")

# Ask the user for a string and print: All unique characters•The count of unique characters
str=input("Enter a string: ")
unique = set(str)
print(f"Unique characters: {unique}")
print(f"Count of unique characters: {len(unique)}")
# for char in unique:
#     print(f"Count of '{char}': {str.count(char)}")
