# f = open("a.txt", "r")  # filename, mode - read-defalut
# f = open("a.txt", "w")  # filename, mode - write-over write
# f = open("a.txt", "a")  # filename, mode - append- write at end
# f = open("a.txt", "x")  # filename, mode - creates new file
# f = open("a.txt", "b")  # filename, mode - binary
# f = open("a.txt", "t")  # filename, mode - text-default
# f = open("a.txt", "+")  # filename, mode - open disk file for update(r&w)

# print(f.read())
# print(type(f.read()))

# print(f.readline())

# f1=open("a1.txt","x")
# f11=open("a.txt","a+")
# f1.write("random")

# d=f.write("\n hello i'm sakshi shah....")
# print(f11.write("\n hello i'm sakshi shah....123!!!"))
# print(f11.read())

# print(d)
# f1.close()
# f11.close()
# f.close()


# with open("a1.txt","a+") as f:  #with -  automatic close ho jayegi, explisitly close krne ki jrurat nhi h
#     ss=f.read()
#     f.write("\n hello i'm sakshi shah....123!!!")
#     print(ss)
#     print(len(ss))

# import os
# os.remove("a1.txt")

# data = True
# line = 1
# word = "roll"
# with open("a1.txt", "r") as f:
#     while data:
#         data = f.readline()
#         if word in data:
#             print(f"found at line {line}")
#             break
#         line += 1


# exception handling- try, except, else, finally
# try:
#     x = int(input("enter x  "))
#     ans = 10 / x
# except ZeroDivisionError:
#     print("divide by zero is not allowed")
# except ValueError:
#     print("invalid input")
# else:
#     print(ans)

# finally:  # always execute weather error occured or not
#     print("it's looks good")


# list comprehensions
# [ op   iteration           condition]
# [i*i   for i in range(6)    if i%2!=0]
print([i * i for i in range(6) if i % 2 != 0])

nums=[-2,1,0,-3,-8,44,6,-9]
print([0 if i < 0 else i for i in nums ]) #conditional output

words=["he","oo","lof"]
print([val.upper() for val in words])


# json module
# dumps()- convert into python
# loads()-convert into json