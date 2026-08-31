def recursion(n):
    if n<1:
        return
    print(n)
    n=n-1
    recursion(n)

n=8
(recursion(n))


def recur(x):
    if x>n:
        return
    # for n in range(n):
    print(x)
    x=x+2
    recur(x)


# n=8

(recur(1))
