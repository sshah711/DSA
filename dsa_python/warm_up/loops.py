for i in range(10):
    print("hi", i)


def demo(i):
    print("hii", i)


for i in range(1, 16, 2):
    # print("hii",i)
    demo(i)

arr = [1, 2, 4, 5, 3, 6, 0]
print(len(arr))
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        print(arr[i])

i = 0
while i < 6:
    print(i, "s")
    i += 1


# x=2
def search_ele(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


a = [1, 2, 5, 3, 6, 4, 7, 0, 44, 32, 21]
print(search_ele(a, 32))


def countss(ar):
    n = 0
    for i in range(len(ar)):
        if ar[i] < 0:
            n += 1
    return n


ar = [-1, 2, -5, 3, -6, 4, -7, 0, -44, 32, 21]
print(countss(ar))


def large_num(Ar):
    l = Ar[0]
    for i in range(len(Ar)):
        if Ar[i] > l:
            l = Ar[i]
    # Ar.sort()
    # return Ar[-1]
    return l


a = [-1, -2, -5, -31, 3]
print(large_num(a))


def small_num(Ar):
    l = Ar[0]
    for i in range(len(Ar)):
        if Ar[i] < l:
            l = Ar[i]
    # Ar.sort()
    # return Ar[-1]
    return l


a = [-1, -2, -5, -31, 3]
print(small_num(a))


# for i in range(6):
#     for j in range(i):
#         print(i)
