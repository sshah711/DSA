def s(a,b):
    sum=a+b
    return sum
a=int(input("1st num "))
b=int(input("2nd num "))
print("sum is" ,s(a,b))


def even_odd(a):
    # if a<0:
    #     print("Negative number")
    if a % 2 == 0:
        print("Even")
    else:
        print("Odd")

a=int(input("Enter a number "))
even_odd(a)
